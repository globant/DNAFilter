import os
import sys

sys.path.append(os.getcwd())

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#activate_this = "../bin/activate_this.py"
#activate_this = "/home/ubuntu/projects/dnafilter/deploydj/bin/activate_this.py"
#activate_this = os.path.join(os.path.dirname(os.getcwd()), "bin/activate_this.py")
activate_this = os.path.join(PROJECT_ROOT, "bin/activate_this.py")
#activate_this = os.path.join(os.getcwd(), "../bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))


os.environ['DJANGO_SETTINGS_MODULE'] = 'dnafilter.settings'

import django.core.handlers.wsgi


application = django.core.handlers.wsgi.WSGIHandler()
