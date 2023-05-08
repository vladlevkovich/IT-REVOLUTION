"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')

application = get_wsgi_application()


# import os
# import sys
# from django.core.wsgi import get_wsgi_application
#
# sys.path.insert(0, sys.path.dirname(os.path.abspath(__file__)))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.production')
#
# if os.environ.get("DJANGO_SETTINGS_MODULE") == "server.settings.production":
#         from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
#         application = Sentry(get_wsgi_application())
# else:
#         get_wsgi_application()
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_wsgi_application()
