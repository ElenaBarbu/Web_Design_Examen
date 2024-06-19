from django.db import models

# Create your models here.
class flight(models.Model):
    airline = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    stopovers = models.BooleanField(default=False)
    specialOffer = models.BooleanField(default=False)
    details = models.CharField(max_length=400)

class train(models.Model):
    company = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    stopovers = models.BooleanField(default=False)
    specialOffer = models.BooleanField(default=False)
    details = models.CharField(max_length=400)

class cruise(models.Model):
    company = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    stopovers = models.BooleanField(default=False)
    specialOffer = models.BooleanField(default=False)
    details = models.CharField(max_length=400)
