
--------------------------------------------------------------------------------------------------------------
python requirements
--------------------------------------------------------------------------------------------------------------

The IMMO project requires python3

To install python3 on a debian version of Linux (such as Ubuntu), issue the following:

    sudo apt update
    sudo apt install python3

You can check the installation with:

    python3 --version

This should output something like:

    Python 3.10.12

The project will require python packages such as the Django framework. Installation of python packages is done with the pip utility.
The pip utility also needs to be installed before installing Django. To install the pip utility, issue the following:

    sudo apt update
    sudo apt install python3-pip

Once the pip utility is installed, Django and other required packages can be installed


--------------------------------------------------------------------------------------------------------------
Creating python virtual environments
--------------------------------------------------------------------------------------------------------------

A virtual environment is a separate installation of python packages. The virtual environment
allows installing and testing versions of packages that are different from the base python installation.
Virtual environments are created with the virtualenv tool. This tool needs to be installed; to install
the virtualenv tool, issue the following:

    pip install virtualenv

The project will be developed within 2 virtual environments:

    immo      --> for the release version
    immo_dev  --> for development

The following instructs on how to create the immo_dev virtual environment; to create the immo_dev virtual environment:

    move to the directory under which the virtual environment is to be created (suppose it's /path/to/dev):

        cd /path/to/dev

    create the virtual environment with:

        python3 -m venv immo_dev

This will create a directory named immo_dev under /path/to/dev. The new /path/to/dev/immo_dev directory will contain:

    bin
    include
    lib
    lib64
    pyenv.cfg

If you look into the /path/to/dev/immo_dev/bin directory, you will see the following:

    drwxrwxr-x 2 zardoz zardoz 4096 Apr 17 10:29 .
    drwxrwxr-x 5 zardoz zardoz 4096 Apr 17 10:29 ..
    -rw-r--r-- 1 zardoz zardoz 1996 Apr 17 10:29 activate
    -rw-r--r-- 1 zardoz zardoz  922 Apr 17 10:29 activate.csh
    -rw-r--r-- 1 zardoz zardoz 2202 Apr 17 10:29 activate.fish
    -rw-r--r-- 1 zardoz zardoz 9033 Apr 17 10:29 Activate.ps1
    -rwxrwxr-x 1 zardoz zardoz  238 Apr 17 10:29 pip
    -rwxrwxr-x 1 zardoz zardoz  238 Apr 17 10:29 pip3
    -rwxrwxr-x 1 zardoz zardoz  238 Apr 17 10:29 pip3.10
    lrwxrwxrwx 1 zardoz zardoz    7 Apr 17 10:29 python -> python3
    lrwxrwxrwx 1 zardoz zardoz   16 Apr 17 10:29 python3 -> /usr/bin/python3
    lrwxrwxrwx 1 zardoz zardoz    7 Apr 17 10:29 python3.10 -> python3


Notice the file named activate; this file holds a program that must be executed with the source command. This
program activates the immo_dev virtual environment; once the virtual environment is activated, python commands are 
executed from within the virtual environment. For example, once the virual environment is activated, using the pip 
command will install packages in the virtual environment (under the /path/to/dev/immo_dev directory), not in the 
base python installation directories. Also, python will use packages from the virtual environment, not the base 
environment.


To switch over to the new immo_dev evironment,

    move to the new virtual environment directory (/path/to/dev/immo_dev in this example):

        cd /path/to/dev/immo_dev

    activate the virtual environment by issuing the source command on the activate program in the bin directory:

        source bin/activate

The command line prompt will reflect that commands are executed from the activated virtual environment:

    (immo_dev) myuser@myhost:~/path/to/dev/immo_dev

To exit (deactivate) the virtual environment, issue the deactivcate command:

     (immo_dev) myuser@myhost:~/path/to/dev/immo_dev$ deactivate

The regular command line prompt will return.


--------------------------------------------------------------------------------------------------------------
Installing Django
--------------------------------------------------------------------------------------------------------------

Django is a python package and will be installed in the immo and immo_dev virtual environments. The following
shows how to insall Django in the immo_dev virtual environment. 

First, activate the immo_dev virtual environment:

    cd /path/to/dev/immo_dev
    source bin/activate

Install Django in the virtual environment

    python3 -m pip install django

If you look in the /path/to/dev/immo_dev/bin directory, you will see a new file named django-admin. This file is a program
that links to the python3 program within the virtual environment. The first line of the program is:

    #!/home/zardoz/immo_dev/bin/python3

The django-admin program is used to create a dlango project. The next step is to create the Django project called immo_dev


--------------------------------------------------------------------------------------------------------------
Creating the immo_dev django project
--------------------------------------------------------------------------------------------------------------

Move to the immo_dev virtual directory and activate it:

    cd /path/to/dev/immo_dev
    source bin/activate

The command line prompt should reflect that the virtual environment is active. To create the immo_dev django project:

    django-admin startproject immo_dev

You will notice that a new immo_dev directory has been created under /path/to/dev/immo_dev:

    drwxrwxr-x  6 zardoz zardoz   4096 Apr 17 12:54 .
    drwxr-x--- 46 zardoz zardoz 114688 Apr 17 11:16 ..
    drwxrwxr-x  2 zardoz zardoz   4096 Apr 17 11:17 bin
    drwxrwxr-x  3 zardoz zardoz   4096 Apr 17 12:54 immo_dev
    drwxrwxr-x  2 zardoz zardoz   4096 Apr 17 10:29 include
    drwxrwxr-x  3 zardoz zardoz   4096 Apr 17 10:29 lib
    lrwxrwxrwx  1 zardoz zardoz      3 Apr 17 10:29 lib64 -> lib
    -rw-rw-r--  1 zardoz zardoz     71 Apr 17 10:29 pyvenv.cfg


Under the new immo_dev directory is another immo_dev directory!!! So we have:

    /path/to/dev/immo_dev                     --> this is our virtual environment (it can be any name)
    /path/to/dev/immo_dev/immo_dev            --> this is the Django project base directory; it will hold 
                                                  application directories and the admin program for the 
                                                  project (manage.py)
    /path/to/dev/immo_dev/immo_dev/immo_dev   --> this directory holds project global settings and related files

In /path/to/dev/immo_dev/immo_dev, we have a program called manage.py; this program will be used for administrative tasks 
such as starting a local web server or to create Django applications. A Django application will typically accept an HTTP 
request and return an HTTP response.

The innermost directory (/path/to/dev/immo_dev/immo_dev/immo_dev) will contain the project's settings (and other information):

    drwxrwxr-x 2 zardoz zardoz 4096 Apr 17 12:54 .
    drwxrwxr-x 3 zardoz zardoz 4096 Apr 17 12:54 ..
    -rw-rw-r-- 1 zardoz zardoz  393 Apr 17 12:54 asgi.py
    -rw-rw-r-- 1 zardoz zardoz    0 Apr 17 12:54 __init__.py
    -rw-rw-r-- 1 zardoz zardoz 3227 Apr 17 12:54 settings.py
    -rw-rw-r-- 1 zardoz zardoz  764 Apr 17 12:54 urls.py
    -rw-rw-r-- 1 zardoz zardoz  393 Apr 17 12:54 wsgi.py

The settings.py file will contain, amongst other things, the information needed to connect to a database (more on this later)

The Django project has a minimal local web server that can be used for testing. The web server 
can be started with:

    move to the immo_dev project (where the manage.py program is):

        cd /path/to/dev/immo_dev/immo_dev

    run the local web server:

        python3 manage.py runserver

Open a web browser and go to address:

    http://127.0.0.1:8000/

A page informing of a successful Django installation should show up.

---------------------------------------------------------------------------------------------
Using Postgre SQL with Django
---------------------------------------------------------------------------------------------

In postgre SQL, if not already done, create the immo_dev dadtabase and create a role for the immo_dev database:

CREATE ROLE immo_dev WITH SUPERUSER LOGIN PASSWORD 'immo_dev';


To access a Postgre SQL database from python, the psycopg2 package must be installed in the virtual environment
(the immo_dev virtual environment must be activated):

    pip install psycopg2


Edit the settings.py file in the project settings directory (/path/to/dev/immo_dev/immo_dev/immo_dev)
There is already a default SQLite database which can be replaced with the Postgre SQL information:

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'immo_dev',
        'USER': 'immo_dev',
        'PASSWORD': 'immo_dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

You can test the database connection by executing the following from the Django project (/path/to/dev/immo_dev/immo_dev):

    python3 manage.py dbshell

This will open Postgre SQL and the output should be like the following:

    psql (16.2 (Ubuntu 16.2-1.pgdg22.04+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
    Type "help" for help.

    immo_dev=#

The above is the Postgre SQL prompt. To exit Postgre SQL and return to the command line, type \q at the Postgre SQL prompt.


Next, create views on the database (assuming the tables have been created in the immo_dev database). From the project 
directory (/path/to/dev/immo_dev/immo_dev), issue the following command to create the models in the project's settings:

    python3 manage.py inspectdb > immo_dev/models.py

This models.py file can be used later to create the individual models.py files for applciations.

---------------------------------------------------------------------------------------------
Extra folder for miscellaneous files
---------------------------------------------------------------------------------------------

An extra folder called misc is created under the project directory to hol miscellaneous 
files such the database DDL script.

---------------------------------------------------------------------------------------------
CORS headers and cross origin errors
---------------------------------------------------------------------------------------------

The front end will be developped with ReactJS using nodejs. The nodejs instance
runs on localhost:3000. If a javascript retrieved from nodejs tries to reach this 
Django application which runs on localhost:8000, Django server will not send 
a Access-Control-Allow-Origin header; the brownser will then block the request. 

We need to tell the browser that requests to localhost:8000 can be accepted from a javascript 
retrieved from localhost:3000. What is needed is a python middleware that 
returns the Access-Control-Allow-Origin HTTP response header to the browser when a javascript
retrieved from origin localhost:3000 makes a request to localhost:8000. 

A python package called jango-cors-headers inserts the required header when required. To install it:

    python3 -m pip install django-cors-headers

In the project settings.py file, add the following:

    INSTALLED_APPS = [
        ...,
        "corsheaders",
        ...,
    ]

    MIDDLEWARE = [
        ...,
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        ...,
    ]

CorsMiddleware should be placed as high as possible,
Add the allowed origins (make sure this is what you really want).
In this case, this is the nodejs instance that runs locally for
ReactJS development:

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
    ]

Now, requests to localhost:8000 from nodejs (localhost:3000) will be allowed by Django.

---------------------------------------------------------------------------------------------
Allowing for POST requests
---------------------------------------------------------------------------------------------

By default, POST requests are blocked by Django (it will return a HTTP 403 response - forbidden).
To allow a page to submit POST requests from Javascript, the following can be done:

In settings.py, add the following:

    CSRF_USE_SESSIONS = False
    CSRF_COOKIE_HTTPONLY = False

This means we want the server to provide a CSRRF token in an HTTP  header. Next, from the 
Javascript, that CFRS token must be returned to the server when the POST rrequest is submitted.
The Javascript code must retrieve the token and send it to the server. To retrieve the
token, the following Javascript function can be called:

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }   
        return cookieValue;
    }

Then, the Ajax function can retrieve the token by callingg the function and sending the 
POST request as in:

    xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {

        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("result").innerHTML =
            this.responseText;
        }
    }

    // This is toretrieve the CSRF token that must be returned
    // to the server when a POST resquest is sent.
    
    const csrftoken = getCookie('csrftoken');

    xhttp.open("POST", "http://localhost:8000/some/route/");
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send(JSON.stringify(data));    


---------------------------------------------------------------------------------------------
Using git
---------------------------------------------------------------------------------------------

inside the project directory, issue the following command:

    git init

This creates a git repository. To see the effect, issue the following command:

    git status

This shows the following:

    On branch master

    No commits yet

    Untracked files:
        (use "git add <file>..." to include in what will be committed)

	        .gitignore
	        db.sqlite3
	        immo_dev/
	        manage.py
	        welcome/

It is a good idea to have a .gitignore file (the dot (.) is important because this needs to be a hidden file);
this file contains the items git must not consider (ignore) when making commits.

    touch .gitignore

Edit the .gitignore file andd add the following:

    manage.py
    db.sqlite3

As an asside, it is a good idea to create a requirrements.txt file. This file will hold the required packages for the project to run.
The requirements.txt file can be created from the project directory by:

    pip freeze > requirements.txt


Finally, add the project to git:

    git add -A

If we do a git status, we get:

    On branch master

    No commits yet

    Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
	        new file:   .gitignore
	        new file:   immo_dev/__init__.py
	        new file:   immo_dev/__pycache__/__init__.cpython-310.pyc
	        new file:   immo_dev/__pycache__/settings.cpython-310.pyc
	        new file:   immo_dev/__pycache__/urls.cpython-310.pyc
	        new file:   immo_dev/__pycache__/wsgi.cpython-310.pyc
	        new file:   immo_dev/asgi.py
	        new file:   immo_dev/settings.py
	        new file:   immo_dev/urls.py
	        new file:   immo_dev/wsgi.py
	        new file:   requirements.txt

Finally, we can commit the changes:

    git commit -m "initial commit"

This should result in the following messages:

    [master (root-commit) aa9b2d0] initial commit
        11 files changed, 202 insertions(+)
        create mode 100644 .gitignore
        create mode 100644 immo_dev/__init__.py
        create mode 100644 immo_dev/__pycache__/__init__.cpython-310.pyc
        create mode 100644 immo_dev/__pycache__/settings.cpython-310.pyc
        create mode 100644 immo_dev/__pycache__/urls.cpython-310.pyc
        create mode 100644 immo_dev/__pycache__/wsgi.cpython-310.pyc
        create mode 100644 immo_dev/asgi.py
        create mode 100644 immo_dev/settings.py
        create mode 100644 immo_dev/urls.py
        create mode 100644 immo_dev/wsgi.py
        create mode 100644 project-readme.txt
        create mode 100644 requirements.txt



