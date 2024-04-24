from django.shortcuts import render
from .models import Route

def index(request):
    return render(request, "gestion/index.html")

def routes(request):
    routes_list = Route.objects.order_by("departure_time")
    return render(request, "gestion/routes.html", {"routes_list": routes_list})