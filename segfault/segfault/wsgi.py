"""
WSGI config for segfault project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import sys

path = '/var/www/backend/segfault/'
if path not in sys.path:
    sys.path.append(path)
    

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'segfault.settings')

application = get_wsgi_application()
