'''
    Settings for develipment environment. Works as an example for building your local.settings.
    
    @author: mCecilia
    @since: 20-02-2013 
'''
from common import * 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'development/path/django_dnafilter2',   #Path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    'development/path/templates',
)


STATIC_PATH = '/var/www/dnafilterD/dnafilter/static'