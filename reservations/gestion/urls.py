from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("routes", views.routes, name="routes"),
    path("trajets", views.routes, name="routes"),
]