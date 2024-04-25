from django.db import models
from django.contrib.auth.models import User

class Station(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
       return self.name

class Passenger(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    
class Route(models.Model):
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='departure_station')
    departure_time = models.DateTimeField()
    arrival_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='arrival_station')
    arrival_time = models.DateTimeField()
    def __str__(self):
       return f"{self.departure_station} | {self.departure_time.strftime('%Y-%m-%d %H:%M')}\
                => {self.arrival_station} | {self.arrival_time.strftime('%Y-%m-%d %H:%M')}"

class Reservation(models.Model):
    reservation_date = models.DateTimeField()
    reservation_number = models.CharField(max_length=10, unique=True)
    seat_number = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)