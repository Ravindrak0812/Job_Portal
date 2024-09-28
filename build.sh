#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Upgrade pip
python -m pip install --upgrade pip

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Check if a superuser should be created
if [ "$CREATE_SUPERUSER" = "True" ]; then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
