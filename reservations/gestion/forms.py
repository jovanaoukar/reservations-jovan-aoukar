from django import forms
from .models import Station


class SearchRouteForm(forms.Form):
    station_choices = [("","Select...")]
    
    departure_station_name = forms.CharField(
        label='Departure Station',
        widget=forms.Select(choices=station_choices),
        max_length=200,
        required=False
        )
    
    arrival_station_name = forms.CharField(
        label='Arrival Station',
        widget=forms.Select(choices=station_choices),
        max_length=200,
        required=False
        )
    
    def __init__(self, *args, **kwargs):
        super(SearchRouteForm, self).__init__(*args, **kwargs)
        self.fields['station_choices'].choices = [("","Select...")] + [(station.name, station.name) for station in Station.objects.all().order_by()]
    