import socket

DEBUG = True

#EXTRA_INSTALLED_APPS = ('debug_toolbar',)
#EXTRA_MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',)

#INTERNAL_IPS = ('127.0.0.1',)


#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '/home/sebastian/Projects/dnafilter/officialrepo/DNAFilter/django_dnafilter2',
        'NAME': 'database.db',           # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

if socket.gethostname() == 'glb7765':
    TEMPLATE_DIRS = (
    '/home/sebastian/Projects/dnafilter/officialrepo/DNAFilter/dnafilter/templates',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/var/www/dnafilterD/dnafilter/templates',
)
