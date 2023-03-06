from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contry = models.CharField(max_length=100)
