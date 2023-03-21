from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

# Create your views here.

tasks = ["alpha", "bravo", "charlie"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

employee = {
    "name" : ["alpha", "bravo"],
    "age" : 39
}

# def tasks(request):
#     global tasks
#     return render(request, "tasks/index.html", {
#         "tasks" : tasks,
#         "hello" : "Hello ",
#         "employee" : employee,
#     })

def tasks(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    # global tasks
    # if request.method == "post":
    #     name = request.form['task']
    #     tasks.tasks.append(name)
    #     employee["name"].append(name)
    #     return HttpResponseRedirect(reverse("tasks:index"))
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form" : form
            })
        
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })
