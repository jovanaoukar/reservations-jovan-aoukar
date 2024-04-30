from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Route, Reservation, Client
from .forms import SearchRouteForm

def index(request):
    return render(request, "gestion/index.html")

# def routes(request):
#     routes_list = Route.objects.order_by("departure_time")
#     return render(request, "gestion/routes.html", {"routes_list": routes_list})

def search_routes(request):
    if request.method == "POST":
        form = SearchRouteForm(request.POST)
        if form.is_valid():
            departure_station_name = form.cleaned_data['departure_station_name']
            arrival_station_name = form.cleaned_data['arrival_station_name']
            routes_list=Route.objects.all()
            if departure_station_name:
                routes_list = routes_list.filter(departure_station__name=departure_station_name)
            if arrival_station_name:
                routes_list = routes_list.filter(arrival_station__name=arrival_station_name)
            routes_list = routes_list.order_by("departure_time", "arrival_time")
    elif request.method == "GET":
        form = SearchRouteForm()
        routes_list = Route.objects.order_by("departure_time", "arrival_time")
    return render(request, "gestion/routes.html", {"routes_list": routes_list, "form": form})

@login_required
def reservations(request):
    user_id = request.user.id
    client = get_object_or_404(Client.objects, user_id=user_id)
    client_reservations_list = Reservation.objects.filter(client=client)
    upcoming_reservations_list = client_reservations_list.filter(route__departure_time__gt=timezone.now())
    actual_reservations_list = client_reservations_list.filter(route__departure_time__lte=timezone.now(), route__arrival_time__gte=timezone.now())
    past_reservations_list = client_reservations_list.filter(route__arrival_time__lt=timezone.now())
    return render(request, "gestion/reservations.html", {"upcoming_reservations":upcoming_reservations_list,
                                                         "actual_reservations":actual_reservations_list,
                                                         "past_reservations":past_reservations_list
                                                         })

@login_required
def reservation(request, reservation_id):
    reserv_obj = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, "gestion/reservation.html", {"reservation":reserv_obj})
