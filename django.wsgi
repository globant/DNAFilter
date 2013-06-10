import os
import sys

sys.path.append(os.getcwd())

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(PROJECT_ROOT)
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
activate_this = os.path.join(PROJECT_ROOT, "bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dnafilter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
