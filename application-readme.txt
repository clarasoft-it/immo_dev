
--------------------------------------------------------------------------------------------------------------
Creating Django applications within the Django project
--------------------------------------------------------------------------------------------------------------

A Django application is a program that runs within the Django framework. Django needs to know which applications
are run under its framework. To create a Django application named welcome (move to /path/to/dev/immo_dev/immo_dev):

    python3 manage.py startapp welcome

This application will simply show a welcome page; a new directory will be created under the project directory:

    ls /path/to/dev/immo_dev/immo_dev

A new directory named welcome has been created:

    drwxrwxr-x 4 zardoz zardoz 4096 Apr 17 14:58 .
    drwxrwxr-x 6 zardoz zardoz 4096 Apr 17 12:54 ..
    -rw-r--r-- 1 zardoz zardoz    0 Apr 17 13:31 db.sqlite3
    drwxrwxr-x 3 zardoz zardoz 4096 Apr 17 13:31 immo_dev
    -rwxrwxr-x 1 zardoz zardoz  664 Apr 17 12:54 manage.py
    drwxrwxr-x 3 zardoz zardoz 4096 Apr 17 14:58 welcome

The new welcome directory has the following files:

    rwxrwxr-x 3 zardoz zardoz 4096 Apr 17 14:58 .
    drwxrwxr-x 4 zardoz zardoz 4096 Apr 17 14:58 ..
    -rw-rw-r-- 1 zardoz zardoz   63 Apr 17 14:58 admin.py
    -rw-rw-r-- 1 zardoz zardoz  146 Apr 17 14:58 apps.py
    -rw-rw-r-- 1 zardoz zardoz    0 Apr 17 14:58 __init__.py
    drwxrwxr-x 2 zardoz zardoz 4096 Apr 17 14:58 migrations
    -rw-rw-r-- 1 zardoz zardoz   57 Apr 17 14:58 models.py
    -rw-rw-r-- 1 zardoz zardoz   60 Apr 17 14:58 tests.py
    -rw-rw-r-- 1 zardoz zardoz   63 Apr 17 14:58 views.py

We now have to add this application to the Django project. In the Django project settings,
open the settings.py file (in /path/to/dev/immo_dev/immo_dev/immo_dev) an add the welcome application
in the INSTALLED_APPS array (list):

Before:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]


After:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'welcome',
    ]


The applciation is actually a set of files, one of which is the views.py file. 
This file will define functions that are called from the Django framework when 
a URL under the web site (http://127.0.0.1:8000/) is specified in the browser.

In particular, the views.py file will define functions that the Django framework will call 
when a URL is specified. The functions will accept an HTTP request and return an HTTP response.
In the views.psy file, define the following function:


    from django.shortcuts import render
    from django.http import HttpResponse

    def show_home_page(request):
        return HttpResponse("Welcome to IMMO!")

--------------------------------------------------------------------------------------------------------------
Using the database
--------------------------------------------------------------------------------------------------------------

If the application uses the database, then models have to be created. Initially, in the project's settings directory,
a models.py file was generated when the project was created. Copy whatever models are required:

First, create a models.py file in the application directory (/path/to/dev/immo_dev/immo_dev/welcome/models.py in this example):

    touch models.py 

From the /path/to/dev/immo_dev/immo_dev/models.py file, copy the required models, for example:

    from django.db import models

    class Contacts(models.Model):
        firstName = models.CharField(primary_key=True, max_length=36, db_comment='First Name')
        lastName = models.CharField(primary_key=True, max_length=36, db_comment='Last Name')
        phone = models.CharField(primary_key=false, max_length=36, db_comment='Phone number')

    class Meta:
        managed = False
        db_table = 'mytable'
        unique_together = (('firstName', 'lastName'),)
        db_table_comment = 'Contacts'


Once the models are created, they must be migrated. From the project directory,

    python manage.py migrate --fake-initial



--------------------------------------------------------------------------------------------------------------
Connecting a URL to the application (an application function actually)
--------------------------------------------------------------------------------------------------------------

If the application is to be executed from a URL, we need to assocaite that URL to a function
implemented in the views.py file. We will associate the URL /home to the function show_home_page
defined above. To do this, we must create a file named urls.py under the application directory:

    cd /path/to/dev/immo_dev/immo_dev/welcome
    touch urls.py

Edit the urls.py file and add the following:

    from django.urls import path
    from .views import show_home_page

    urlpatterns = [
        path("", show_home_page, name="home"),
    ]

Finally, we must update the project's urls.py file (this file was automatically created with the project
so there is no need to create it). Edit the project's urls.py file (in /path/to/dev/immo_dev/immo_dev/immo_dev)
and add an import and call to path() in the urlpatterns list (array):


Before:

    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]

After:

    from from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('home', include("welcome.urls"))
    ]


The welcome page sould now be shown when the user writes the following URL in a browser:

    http://127.0.0.1:8000/home

These are the basic steps to create a web application with Django. 


