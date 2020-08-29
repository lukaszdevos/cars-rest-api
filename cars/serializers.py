from rest_framework import serializers
from cars.models import Car, RateCar
from django.db.models import Avg, Sum, Count

class CarSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ('car_make', 'model_name', 'rate')

    def get_rate(self, get_object ):
        car_avg = get_object.car.aggregate(Avg('rate')).get('rate__avg')
        return car_avg

class RateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCar
        fields = ('rate', 'car')

class CarPopularSerializer(serializers.ModelSerializer):
    rateing_count = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ('car_make', 'model_name', 'rateing_count')

    def get_rateing_count(self, get_object ):
        rateing_count = get_object.car.aggregate(Count('rate')).get('rate__count')
        return rateing_count
