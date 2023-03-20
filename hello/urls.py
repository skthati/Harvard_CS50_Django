# from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sandeep", views.sandeep, name="sandeep"),
    path("namespage", views.names, name="namespage"),
    path("<name>", views.greet, name="greet")
    
]
