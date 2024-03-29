"""
WSGI config for meaqua project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from meaqua.info import log_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meaqua.settings')

application = get_wsgi_application()

log_settings()
