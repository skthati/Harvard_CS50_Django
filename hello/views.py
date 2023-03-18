from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "names/index.html")

def sandeep(request):
    return HttpResponse("Hello Sandeep!")

def greet(request, name):
    return HttpResponse(f"Hello {name.title()}!")

def names(request):
    return render(request, "names/index.html")
