#!/bin/sh

/opt/venv/bin/python manage.py migrate --no-input
/opt/venv/bin/python manage.py collectstatic --no-input

# /opt/venv/bin/gunicorn superlink.wsgi:application --bind 0.0.0.0:8000
/opt/venv/bin/python manage.py runserver 0.0.0.0:8000
