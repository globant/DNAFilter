DNAFilter
=========

Setup
-----

# Creates the database tables

django-admin.py syncdb
Creates the database tables for all apps in INSTALLED_APPS whose tables have not already been created.

Use this command when you've added new applications to your project and want to install them in the database. 
This includes any apps shipped with Django that might be in INSTALLED_APPS by default. 
When you start a new project, run this command to install the default apps.

# Apache & mod_wsgi

Virtual Host:

    <VirtualHost *:80>
        ServerAdmin webmaster@localhost

        DocumentRoot /var/www/dnafilterD

        WSGIScriptAlias / /var/www/dnafilterD/django.wsgi

        <Directory /var/www/dnafilterD>
        Options -Indexes
        Order allow,deny
        allow from all
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/dnafilter_error.log

        # Possible values include: debug, info, notice, warn, error, crit,
        # alert, emerg.
        LogLevel warn

        CustomLog ${APACHE_LOG_DIR}/dnafilter_access.log combined

    </VirtualHost>
