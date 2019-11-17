


///////////////////
# Setup bits

 sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  python3 -m venv venv
 sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  code .
 sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  pip list
zsh: command not found: pip
 ✘ sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  source venv/bin/activate
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  pip list
Package       Version
------------- -------
pip           18.1   
pkg-resources 0.0.0  
setuptools    40.8.0 
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  pip install django

Collecting django
  Downloading https://files.pythonhosted.org/packages/a0/36/463632a2e9161a7e713488d719a280e8cb0c7e3a66ed32a32e801891caae/Django-2.2.7-py3-none-any.whl (7.5MB)
    100% |████████████████████████████████| 7.5MB 125kB/s 
Collecting sqlparse (from django)
  Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
    100% |████████████████████████████████| 512kB 1.3MB/s 
Installing collected packages: sqlparse, pytz, django
Successfully installed django-2.2.7 pytz-2019.3 sqlparse-0.3.0
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  ls
venv
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  pip list 
Package       Version
------------- -------
Django        2.2.7  
pip           18.1   
pkg-resources 0.0.0  
pytz          2019.3 
setuptools    40.8.0 
sqlparse      0.3.0  
(venv)  ✘ sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  django-admin startproject djangoapp 
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app  cd djangoapp 
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app/djangoapp  ls
djangoapp  manage.py
////////////////
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app/djangoapp   master  python manage.py 

Type 'manage.py help <subcommand>' for help on a specific subcommand.


# Start Server
(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app/djangoapp   master  python manage.py runserver


//////////////
# DB Migrations
python manage.py migrate
# Create User
python manage.py createsuperuser --username=serg --email=vasiliok@gmail.com

// password


///////

(venv)  sergio@sergio-Latitude-E6420  ~/environments/Web/Django-app/djangoapp   master  python manage.py startapp posts


from django.shortcuts import render
from django.http  import HttpResponse
def index(request):
    return HttpResponse('Hello from posts')