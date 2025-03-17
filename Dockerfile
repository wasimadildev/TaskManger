FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn whitenoise

# Create directory structure first
RUN mkdir -p staticfiles

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=task_management.production
ENV SECRET_KEY="django-insecure-production-key-change-this"
ENV PORT=8000

# Collect static files with error handling
RUN python manage.py collectstatic --noinput || (echo "Collectstatic failed, checking directory structure" && \
    ls -la && \
    echo "Checking static file settings" && \
    grep -r "STATIC" task_management/production.py && \
    exit 1)

EXPOSE 8000

CMD ["gunicorn", "task_management.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"] 