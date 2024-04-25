from django.contrib import admin

from .models import Station, Route, Client, Reservation

admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Client)
admin.site.register(Reservation)

