from django.db import models

class Car(models.Model):
    car_make = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.car_make + ' - ' + self.model_name


#vote scale <1:5>
vote_choices = [(i, i) for i in range(1, 6)]

class RateCar(models.Model):
    rate = models.IntegerField(choices=vote_choices)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')

    def __str__(self):
        return self.car.car_make + ' - ' + self.car.model_name + ' rate: ' + str(self.rate)

    