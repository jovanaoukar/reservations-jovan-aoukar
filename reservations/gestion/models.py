from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=200)

class Passenger(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    

