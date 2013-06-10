#!/usr/bin/python
'''
    Changelog:
    .2013-02-25|mCecilia: Change settings import. Now you have to import the 
    settings file according to the enviorment where you are working (local, prod, etc).
    Changelog:
    .2013-07-09|sbassi: Import a settings.py file, and a local_settings.py 
    only if present.
    
'''
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError, e:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.stderr.write("Exception Message: %s" % e.message)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
