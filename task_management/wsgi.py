"""
WSGI config for task_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Default to production settings when deployed
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.production')

application = get_wsgi_application()
