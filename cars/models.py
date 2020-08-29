from django.db import models

class Car(models.Model):
    car_make = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.car_make + ' - ' + self.model_name

