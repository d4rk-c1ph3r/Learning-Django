To check the Running version of Django
```
python -m django --version
```

Installing Django
```
pip install django
```

Creating a Project

```
django-admin startproject myproject
```

Starting a Project

```
python manage.py runserver
```

Files inside the project

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
`manage.py` - A command-line utility that lets you interact with this Django project in various ways.
`__init__.py` - python package
`settings.py` - configuration of project
`urls.py` - url endpoints  
`wsgi.py` - entrypoint for wsgi compatible server gateway interface
`asgi.py` - entrypoint for asgi compatible server gateway interface



**APP vs Project**

The main django project(website) contains several apps(pages)

Starting an app

```
python manage.py startapp home
```


App file structure
```
home/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```


Basic views.py
```

from django.http import HttpResponse

def home(response):
	return HttpResponse("Hello World of Python")

```

Create a urls.py in the app directory to make URLconfs

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The next step is to point the root urlconf to the app.urls

```
path('myapp/',include('myapp.urls'))
```
--------------------

**MVT(Model, Views and Templates)**

Design pattern used by django. It is a software design pattern.
M,V and T stands for Models, View and Templates

Also we have MVC(Model,View and Controller) pattern.

Views talks to Models(data) and Template.

**Note: Make sure to note the path and '/' .**


Inside the path in app views file no need to add '/' to path

## Django Template Engine (DTL) and Templates

```
return render(request, 'home.html')
```

To use a template inside the project settings.py add the TEMPLATE DIR.


Template is kept at the same level as manage.py


```
	|- Django project
	   |--urls.py
	   |--settings.py
	   |-- app1
	   |-- app2
	   |-- static
	        |--- css
	        |--- images
	        |--- js
	        	|---- node_modules
	        	|----- foundation-sites
	        	|----- grunt
            	|---- packages.json
	
```


Copy the bootstrap starter template to integrate bootstrap easily.

Navbar bootstrap
Caraousel/Slider bootstrap

Best place to add images from [Unsplash API](https://source.unsplash.com/)

**Use relative links and filepaths to create the design using bootstrap**


# Models and Migrations

Inside models.py create a class for each table of database

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

is similar to 

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```

Take data from form into a dictionary called request.POST. The several keys of this dictionary contains of critical data.

{% csrf_token %} is used to insert a CSRF token.


```
python manage.py makemigrations
```

generates some files which are called migrations. These migrations are use to create tables using the models

```
python manage.py migrate
```

Creates the database tables.

import the models inside the views.py
```
from home.models import Contact
```

Also add the app to installed apps in settings.py

```
ins = Contact(name=name,email=email,phone=phone,comment=comment)
ins.save()
```

Migrations -

Migrate    -


# Django Admin

Register the models inside admin.py to see it in django admin.

Inside admin.py
```
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
```

Creating the admin

```
python manage.py createsuperuser
```

Test project password used is 

```
admin:admin
```

visit the djangoadmin in /admin

Its also possible to create regular users

# customize django admin

Add this inside the `models.py` classes to show the name of the object instead of objectname

```
def __str__(self):
        return self.name
```

Inside `urls.py` use this to change the site headers

```
# Django admin Header Customization
admin.site.site_header='D4rk-c1ph3r'
admin.site.site_title='Admin | D4rk-c1ph3r'
admin.site.index_title='Welcome to D4rk-c1ph3r Devloper Administration'

```

# Hosting Static files

Add STATICFILES_DIR for hosting static files inside `settings.py`

```
import os
STATICFILES_DIRS=[
   os.path.join(BASE_DIR,'static') 
]
```

At the top of the html load the static contents using

```
{% load static %}
```

To reference the static files use

```
{% static '/img/slider1.jpeg' %}
```

# Template Inheritance

Create base.html with the main template

Include this code in the main body

```
    {% block body%}
    {% endblock body%}
```

In the other file use 

```
{% extends 'base.html' %}
{% load static %}
```

The body of the html will be included in the following.
```
    {% block body%}
    {% endblock body%}
```

To add title to pages
```
    {% block title%}
    {% endblock title%}
```

Then add the title in the child html files 

```
    {% block body%}Child title {% endblock body%}
```
