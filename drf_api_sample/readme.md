DRF API Sample
==============
A simple playground for messing around with REST APIs 

1) create venv: `python3 -m venv ~/venv/drf_sample`
2) enable venv: `source ~/venv/drf_sample/bin/activate`
3) install pip/pipenv: `python3 -m pip install --upgrade pip pipenv`
4) `pipenv install`

5) create db:
`python manage.py migrate`
6) create admin account
`python manage.py createsuperuser`

7) drf_yasg / swagger ui has been included as part of this sample, so you can execute REST api calls via: 
`python manage.py runserver localhost:8000/swagger`

8) check in admin view that the log has been added after call to your REST api:
`http://localhost:8000/admin/rest_framework_tracking/`

Development:
------
To install drf_api_tracking for development use:

`pipenv install -e ../../drf_api_tracking`

Note this is already configured in the Pipfile


