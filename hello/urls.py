# from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sandeep", views.sandeep, name="sandeep"),
    path("<name>", views.greet, name="greet"),
    path("names", views.names, name="names")
]
