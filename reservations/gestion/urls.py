from django.urls import path

from . import views

app_name = "gestion" 
urlpatterns = [
    path("", views.index, name="index"),
    path("routes", views.search_routes, name="routes"),
    path("trajets", views.search_routes, name="routes"),
]