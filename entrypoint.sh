#!/bin/sh

python manage.py migrate --no-input

opt/venv/bin/gunicorn superlink.wsgi:application --bind 0.0.0.0:8000
