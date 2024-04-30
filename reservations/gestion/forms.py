from django import forms
from .models import Station


class SearchRouteForm(forms.Form):
    departure_station_name = forms.ModelChoiceField(
        Station.objects.all().order_by("name"),
        empty_label = "Select...",
        to_field_name = "name",
        required = False
    )
    arrival_station_name = forms.ModelChoiceField(
        Station.objects.all().order_by("name"),
        empty_label = "Select...",
        to_field_name = "name",
        required = False
    )
    