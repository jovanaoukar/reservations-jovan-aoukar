from django.contrib import admin

from .models import Station, Route, Client, Passenger, Reservation

admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Client)
admin.site.register(Passenger)
admin.site.register(Reservation)

