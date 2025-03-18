#!/bin/bash
# Exit on error
set -e

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn
exec gunicorn task_management.wsgi:application --bind 0.0.0.0:${PORT:-8000} 