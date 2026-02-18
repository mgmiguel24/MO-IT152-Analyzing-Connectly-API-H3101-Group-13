# wsgi.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# WSGI = Web Server Gateway Interface
# This is the file that connects Django to a web server.
# You will almost never need to touch this file.
# Think of it as the electrical socket that plugs Django into the internet.
# -------------------------------------------------------

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectly_project.settings')
application = get_wsgi_application()
