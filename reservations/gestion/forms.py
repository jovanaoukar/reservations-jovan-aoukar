from django import forms
from .models import Station


class SearchRouteForm(forms.Form):
    station_choices = [(station.name, station.name) for station in Station.objects.all().order_by("name")]
    
    departure_station_name = forms.CharField(
        label='Departure Station',
        widget=forms.Select(choices=station_choices)
        )
    
    arrival_station_name = forms.CharField(
        label='Arrival Station',
        widget=forms.Select(choices=station_choices),
        max_length=300
        )
    