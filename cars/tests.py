from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car, RateCar
from cars.serializers import CarSerializer, RateCarSerializer


class CarsAppTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.car_url = reverse('cars:cars-list')
        self.rate_url = reverse('cars:rate-list')
        self.popular_url = reverse('cars:popular-list')
        self.car_list_qs = Car.objects.all()
        self.ratecar_list_qs = RateCar.objects.all()
        self.car0 = Car.objects.create(car_make='honda', model_name='accord')
        self.car1 = Car.objects.create(car_make='BMW', model_name='m5')
        self.car2 = Car.objects.create(car_make='audi', model_name='a4')
        RateCar.objects.create(car=self.car1, rate=5)
        RateCar.objects.create(car=self.car1, rate=1)
        RateCar.objects.create(car=self.car2, rate=5)
        RateCar.objects.create(car=self.car0, rate=3)
        RateCar.objects.create(car=self.car0, rate=1)
        RateCar.objects.create(car=self.car0, rate=2)

    def test_cars_list(self):
        response = self.client.get(self.car_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        self.assertEqual(response.data['count'], self.car_list_qs.count())
        self.assertEqual(response.data['results'][0]['rate'], 2)
        self.assertEqual(response.data['results'][1]['rate'], 3)
        self.assertEqual(response.data['results'][2]['rate'], 5)

    def test_post_car(self):
        load_data = {'car_make': 'fiat', 'model_name': '500'}
        response = self.client.post(self.car_url, load_data)
        load_data['rate'] = None
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(response.data, load_data)
        
    def test_post_fake_car(self):
        load_data = {'car_make': 'fake_name', 'model_name': 'fake_model'}
        load_empty_data = {'car_make': '', 'model_name': ''}
        response = self.client.post(self.car_url, load_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 
        self.assertEqual(response.data, {'message': 'Car make/Car model does not exists'})
        response_empty_data = self.client.post(self.car_url, load_empty_data)
        self.assertEqual(response_empty_data.data, {'message': 'Car make and Car model name are required.'})


    def test_post_exists_car(self):
        response_get = self.client.get(self.car_url)
        self.assertEqual(response_get.data['count'], 3)
        load_data = {'car_make': 'jeep', 'model_name': 'cherokee'}
        response = self.client.post(self.car_url, load_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_get = self.client.get(self.car_url)
        self.assertEqual(response_get.data['count'], 4)
        response = self.client.post(self.car_url, load_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        response_get = self.client.get(self.car_url)
        self.assertEqual(response_get.data['count'], 4)


    def test_rate_car_GET(self):
        response_get = self.client.get(self.rate_url)
        self.assertEqual(response_get.status_code, status.HTTP_405_METHOD_NOT_ALLOWED )

    def test_rate_car_POST(self):
        self.assertEqual(self.ratecar_list_qs.filter(car=self.car1.id).count(), 2)
        load_data = {'car': self.car1.id, 'rate': 3}
        response = self.client.post(self.rate_url, load_data )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, load_data)
        self.assertEqual(self.ratecar_list_qs.filter(car=self.car1.id).count(), 3)

    def test_popular_car(self):
        response = self.client.get(self.popular_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        self.assertEqual(response.data['count'], self.car_list_qs.count())
        self.assertEqual(response.data['results'][0]['rateing_count'], 3)
        self.assertEqual(response.data['results'][1]['rateing_count'], 2)
        self.assertEqual(response.data['results'][2]['rateing_count'], 1)

    def check_api_nhtsa_works(self):
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/audi?format=json'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        