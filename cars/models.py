from django.db import models

class Cars(models.Model):
    car_brand = models.CharField(max_length=255)
    car_name = models.CharField(max_length=255)
    car_type = models.CharField(max_length=255)
    car_year = models.CharField(max_length=255)
    car_price = models.CharField(max_length=255)

    def __str__(self):
        return self.car_name
