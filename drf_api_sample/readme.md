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

7) run: 
`python manage.py runserver localhost:8000`

Tasks:
------
To install drf_api_tracking for development use:
`pipenv install -e ../../drf_api_tracking`

And include a local version for drf_api_tracking: 
(for reference see: https://docs.djangoproject.com/en/3.0/intro/reusable-apps/)

`python -m pip install --user drf-api-tracking/dist/drf-api-tracking-1.6.0.tar.gz`

To uninstall the package: 

`python -m pip uninstall drf-api-tracking`

Then following the instructions on how to add drf-api-tracking into this project

