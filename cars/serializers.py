from rest_framework import serializers
from cars.models import Car

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('car_make', 'model_name')