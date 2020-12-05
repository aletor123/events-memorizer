#!/bin/bash

python manage.py migrate
sudo apt-get install python-dev libpq-dev
exec "$@"