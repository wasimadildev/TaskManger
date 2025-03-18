#!/bin/bash
# Exit on error
set -e

echo "Starting deployment process..."

# Apply migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Wait a moment to ensure system is ready
echo "Waiting for system to be ready..."
sleep 5

# Start gunicorn
echo "Starting Gunicorn server..."
exec gunicorn task_management.wsgi:application --bind 0.0.0.0:${PORT:-8000} --timeout 120 --workers 2 