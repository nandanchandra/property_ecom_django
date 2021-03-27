# WSGI - Web Server Gateway Interface

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propecom.settings')

application = get_wsgi_application()