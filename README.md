<a name="readme-top"></a>
<div align="center">
<!-- Title: -->

  <h1><a href="https://github.com/skthati/Harvard_CS50_Django">Harvard CS50</a> - Python Django</h1>

<!-- Short description: -->
  <h3>Pratice excercises from CS50 Django class.</h3>
</div>

Django installation.


# Basics

## Django version
To check the version of django

```Python
% python3 -m django --version
```

## Pip version
To check the version of pip

```Python
% python3 -m pip --version
```

## Install Django

To install django, Go into folder where you want to install django and use command

```Python
% django-admin startproject cs50_first_project
```

The above command will create another folder. 

If you want to install in same folder use `" ."` (space dot) after the project name.

```Python
% django-admin startproject cs50_first_project .
```

## Run Django 

```Python
% python3 manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Start new app

Django can contain multiple apps for different purposes and to create new app in present project.

```Python
% python3 manage.py startapp hello
```

The above command will create a new app called "hello" in the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Install hello app

To install the "hello" app which we have created, Go to settings (settings.py) and add below line

```Python
INSTALLED_APPS = [
    'hello',
    'other apps which are already installed'
]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Return response from hello app

Go to hello folder, open views.py

```Python
def index(request):
    return HttpResponse("Hello World from Hello app.")

```

## URL for hello app

Create new file urls.py in hello folder. Add below code.

```Python
urlpatterns = [
    path("", views.index, name="index")
]
```

name is usefull to access different parts of the app and makes easy to reference.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Add reference to main URL

Go to urls.py in main folder and add below line

```Python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls"))
]
```

include(hello.urls) will include all urls from the hello app if someone goes to /hello

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Custom Greet URL
1. Go to views.py and add below code. title() changes to Title case.
    ```Python
    def greet(request, name):
        return HttpResponse(f"Hello {name.title()}!")
    ```
2. Go to urls.py in home folder and add below code.
    ```Python
    urlpatterns = [
    path("", views.index, name="index"),
    path("<name>", views.greet, name="greet")
    ]
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Render HTML
1. Go to views.py and add below code.
    ```Python
    def index(request):
        return render(request, "names/index.html")
    ```
2. Add templates folder, init add home folder, init add index.html. We can add without home folder also but if we have more index.html files this folder can distinguish which index.html we are refering.
    ```Python
    <!DOCTYPE html>
    <html>
    <body>

    <h1>Html Page.</h1>

    <p>Hello</p>

    </body>
    </html>
    ```
3. Go to urls.py in home folder and add below code.
    ```Python
    urlpatterns = [
    path("", views.index, name="index"),
    path("names", views.names, name="names")
    ]
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Check if today is New Year
Simple newyear app which checks if today is new year.

Follow above steps which we used to create hello app and create new app, register in settings, create urls.py and update views.py

Code which checks if today's day is new year or not.views.py

```Python
def newyear(request, name):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "name" : name,
        "datetime" : now.month == 1 and now.day == 1,
        "year" : now.year,
        "month" : now.month,
        "day" : now.day
        
    })
```
Code in index.html. Folder location newyear/templates/newyear/index.html
```Python
{%if datetime%}
    <p>Today is New Year!</p>
{% else %}
    <p>Today is not New Year!</p>
{% endif %}
```

Output

![check new year output image](images/check_newyear.png)



# layouts

Layouts is html template used to eliminated repeated code and very useful altering html content.

Create a file named `layout.html` in templates folder and copy below code.

`layout.html`
```Python
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>

    <body>
        {% block body %}
        {% endblock body %}
    </body>
</html>
```

`index.html`
```Python
{% extends 'layout.html' %}

{% block body %}
    <p> Page specific content here. </p>
{% endblock body %}
```

`{% block any_name %} and {% endblock any_name %}` are used to eliminate repeated content.


# Tasks App
By following hello app and newyear app, create all routine steps

1. Create new app Tasks using `python3 manage.py startapp tasks`
2. Register app in settings.py
3. Create function in views.py
4. Add reference in main urls.py
5. Add url path in local urls.py for the newly created function.
6. Create html in templates folder

## Create a list

`views.py`

```Python
def tasks(request):
    tasks = ["alpha", "bravo", "charlie"]
    return render(request, "tasks/index.html", {
        "tasks" : tasks,
        "hello" : "Hello ",
        "employee" : employee,
    })
```

## index html page
Iterate through tasks list to show list or dictionary.

`index.html`
```Python
{% extends 'layout.html' %}

{% block body %}
    <h1> Tasks </h1>
        <ul>
            
            {% for i in tasks %}
                <li>{{ i }}</li>
            {% endfor %}
        </ul>
    
    {% for i, j in employee.items %}
        {{ i }} : {{ j }}
    {% endfor %}

    <a href="{% url 'tasks:add' %}"> Add a new task </a>
{% endblock body %}
```

## add html page

`add.html`
```Python
{% extends 'layout.html' %}

{% block body %}
<h1>Add Task </h1>

<form action="">
    <input type="text" name="task">
    <input type="submit"> 
</form>

<a href="{% url 'index' %}"> Back to Tasks </a>
{% endblock body %}
```

## To post a form

`add.html`
```Python
<form action="{% url 'tasks:add' %}" method="post">
    {% csrf_token %}
    <input type="text" name="task">
    <input type="submit"> 
</form>
```
csrf token is to prevent CSRF attacks.

# Final code and Output


[index.html](tasks/templates/tasks/index.html)

![Alt text](images/list.png)


Below is the html page and output picture.

[add.html](tasks/templates/tasks/add.html)

![Alt text](images/add_task.png)


# views.py

```Python
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
```
