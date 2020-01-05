"""
WSGI config for library_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
f"""rom dotenv import load_dotenv"""
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
load_dotenv(os.path.join('/Users/andrewporritt/python-django/library_project', '.env'))

application = get_wsgi_application()
