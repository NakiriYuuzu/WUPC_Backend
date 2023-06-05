#!/bin/bash

echo "********** Apply database migrations **********"
python manage.py migrate

echo "********** Running DjangoWebserver **********"
python manage.py runserver 0.0.0.0:80

exec "$@"