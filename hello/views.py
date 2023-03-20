from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, Response from index method")

def sandeep(request):
    return HttpResponse("Hello sandeep!")

def greet(request, name):
    return HttpResponse(f"Hello {name.title()}!")

def names(request):
    return render(request, "names/index.html")
