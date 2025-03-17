"""
Production settings for task_management project.
"""

import os
import dj_database_url
from .settings import *  # Import base settings

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allow all hosts in production (Railway will handle this)
ALLOWED_HOSTS = ['*']

# Use PostgreSQL database in production
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional locations of static files - make sure these directories exist
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tasks', 'static'),
]

# WhiteNoise configuration for production
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Railway handles this
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Simplified logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
} 