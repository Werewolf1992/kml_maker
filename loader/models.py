from __future__ import unicode_literals
from django.db import models


class Store(models.Model):
    city = models.CharField(max_length=100)
    voivodeship = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()