#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata tasks/seed_data.json
exec "$@"
