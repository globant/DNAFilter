import os
import sys

sys.path.append(os.getcwd())

activate_this = "../bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))


os.environ['DJANGO_SETTINGS_MODULE'] = 'dnafilter.settings'

import django.core.handlers.wsgi

#activate_this = os.path.join(path_to_my_site, "../bin/activate_this.py")


application = django.core.handlers.wsgi.WSGIHandler()
