from rest_framework import viewsets, mixins
from cars.serializers import CarSerializer, RateCarSerializer, CarPopularSerializer
from cars.models import Car, RateCar
from rest_framework import status
from rest_framework.response import Response
import requests
from cars.validation import car_validator, exists
from django.db.models import Count



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        request_post_car_make = request.data['car_make'].upper()
        request_post_car_model = request.data['model_name'].capitalize()
        get_car_object = self.queryset.filter(model_name=request_post_car_model.lower(), car_make=request_post_car_make.lower())
        if  get_car_object.exists():
            serializer = CarSerializer(get_car_object[0])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if exists(request_post_car_make, request_post_car_model): 
                if car_validator(request_post_car_make, request_post_car_model):
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Car make/Car model does not exists'}, status=status.HTTP_400_BAD_REQUEST)
            else: 
                return Response({'message': 'Car make and Car model name are required.'})

class RateCarView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = RateCar.objects.all()
    serializer_class = RateCarSerializer


class PopularCarView(viewsets.GenericViewSet , mixins.ListModelMixin):
    queryset = Car.objects.all().annotate(rateing_count=Count('car__rate')).order_by('-rateing_count')
    serializer_class = CarPopularSerializer

   