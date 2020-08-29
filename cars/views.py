from rest_framework import viewsets
from cars.serializers import CarSerializer
from cars.models import Car
from rest_framework import status
from rest_framework.response import Response
import requests, json


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        request_post_car_make = request.data['car_make'].upper()
        request_post_car_model = request.data['model_name'].capitalize()

        url_make_name = 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json'
        url_model_name = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/'+request_post_car_make+'?format=json'
        r_make_name = requests.get(url_make_name)
        r_model_name = requests.get(url_model_name)
        response_dict_make_name = json.loads((r_make_name.text))
        response_dict_model_name = json.loads((r_model_name.text))
        results_for_make_name = response_dict_make_name['Results']
        results_for_model_name = response_dict_model_name['Results']

        make_name = []
        model_name = []
        for i, j in results_for_make_name, results_for_model_name:
            make_name.append(i['Make_Name'])
            model_name.append(j['Model_Name'])


        if request_post_car_make in make_name:
            print('działa???????????????')
            print(request_post_car_make + 'find in database')
        else: 
            print(request_post_car_make)
            print('nie dziala!!!!!!!!!!!!!!!!!')
            




        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)







# url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
# post_fields = {'format': 'json', 'data':'3GNDA13D76S000000;5XYKT3A12CG000000'}
# r = requests.post(url, data=post_fields)
# print(r.text)

# 'modele aut'
# 'https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json'

# 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{{MODELAUTA}}?format=json'