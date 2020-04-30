<<<<<<< HEAD
"""
WSGI config for cocoa project..

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocoa.settings')

application = get_wsgi_application()
=======
"""
WSGI config for cocoa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocoa.settings')

application = get_wsgi_application()
>>>>>>> 96796145ca85fd24ac2c9a6571d58d5f330cfb22
