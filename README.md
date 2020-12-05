# Site checker
Techtask for checking site statuses from 'Website-2020-12-03.xlsx' file.
Checking runs every 15 minutes with celery in background

# Packages
* Django
* DRF
* Celery
* Redis
* Docker

# How to run
Run `docker-compose run django python manage.py migrate` and `docker-compose up`.
Locate results [here](localhost:8000/api/site_check/)
