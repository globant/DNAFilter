'''
    Settings for production environment.
    Gets default values from common.py
    
    @author: mCecilia
    @since: 20-02-2013 
'''
from common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#Configure production data.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/var/www/dnafilterD/django_dnafilter2',   # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/var/www/dnafilterD/dnafilter/templates',
)

STATIC_PATH = '/var/www/dnafilterD/dnafilter/static'