import datetime
from django.shortcuts import render

# Create your views here.

def newyear(request, name):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "name" : name,
        "datetime" : now.month == 1 and now.day == 1,
        "year" : now.year,
        "month" : now.month,
        "day" : now.day
        
    })