import os
import sys

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'dnafilter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
