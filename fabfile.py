# -*- coding: utf-8 -*-
#
# Name: Fabric deployment script for Django DNAFilter app
# Author: Maximiliano Cecilia
# Based on: 
#   Tomaž Muraus (http://www.tomaz-muraus.info)
#   Gareth Rushgrove deployment script (http://morethanseven.net/2009/07/27/fabric-django-git-apache-mod_wsgi-virtualenv-and-p/)
# Version: 1.0
# License: GPL

# Requirements:
# - Linux 
# - Python >= 2.6 (< 3.0)
# - Fabric Python library - tested with 1.6
#
# Project directory structure:
# 
# project_name/
#    app1/
#        __init__.py
#        admin.py
#        models.py
#        tests.py
#        ....
#    app2/
#        __init__.py
#        admin.py
#        ...
#    settings/
#        common.py
#        local.py
#    __init__.py
#    manage.py
#    urls.py
#    requirements.txt
#    project_name.wsgi
#    ...
#    
# And then you would deploy your application by following this steps:
#
# 1. fab <environment> setup - creates a new Python virtual environment and folders for your application - To be implemented.
# 3. fab <environment> deploy_site - deploys your application**
#
# ** "deploy_site" runs the following tasks:
#
# 1. Downloads the latest version of you application from local Git repository to the deploy_path
# 2. Installs the modules required by your application (listed in requirements.txt)
# 3. symbolic links should be already created
# 4. runs syncdb from your project
# 5. Reloads the Apache server
import os
import sys
import posixpath

from fabric.api import env, local, run, sudo, put, cd, runs_once, prompt, require, settings
from fabric.contrib.files import exists, upload_template
from fabric.contrib.console import confirm
from fabric.context_managers import hide, prefix

env.project_directory = '/root/DNAFilterM'
env.project_name = 'DNAFilter'

#Tasks
def say_hello():
    print "Hello World! If you can see this, then fabric is instaled correctly."

# Environments
def production():
    "Set Production environment"
    
    # General settings
    # TODO: Retrieve this data from a non versioned source.
    env.hosts = [] # One or multiple server addresses in format ip:port
    env.user = '' # Username used when making SSH connections
    env.password = '' # Connection and sudo password (you can omit it and Fabric will prompt you when necessary)
    env.www_user = 'www-data' # User account under which Apache is running
    env.virtualenv = '~/virtualenvs/dnafilter.bmhid.org.ar' #virtualenv path
    env.deploy_path = '/root/DNAFilterM/releases' #Path where git project will be downloaded
    env.settings_path = '/root/DNAFilterM/local-settings' #Path for src.
    env.git_url = 'https://github.com/globant/DNAFilter' #URL from git project.
    
def deploy_site():
    """
    Deploy the latest version of the site to the server, install any
    required third party modules and reload the Apache.
    """
    require('hosts', provided_by = [production])

    import time
    env.release = time.strftime('%Y%m%d%H%M%S')

    _upload_archive_from_git()
    _install_requirements()
    _update_settings()
    _create_database_schema()
    _reload_apache()

def setup():
    "Create a new Python virtual environment and folders where our application will be saved. Create project dir and clone it from github"
    require('hosts', provided_by = [production])
    require('deploy_path')
    
    sudo('easy_install pip')
    sudo('pip install virtualenv')
    sudo('mkdir -p %(virtualenv)s; cd %(virtualenv)s; virtualenv --no-site-packages .'  % {'virtualenv': env.virtualenv})
    sudo('chown -R %(user)s:%(user)s %(virtualenv)s'  % {'user': env.user, 'virtualenv': env.virtualenv})
    sudo('mkdir -p %(project_directory)s; cd %(project_directory)s; git clone %(git_url)s'  % {'git_url' : env.git_url, 'project_directory' : env.project_directory})
    
# Helpers - these are called by other functions rather than directly
def _upload_archive_from_git():
    "Create an archive from the current Git master branch and upload it"
    require('release', provided_by = [deploy_site])
    
	# put master branch into release as a zip.
    local('git archive --format=zip master > %(release)s.zip' % {'release': env.release})
	# limpio el directorio actual
    run('rm -rf %(deploy_path)s/*' % {'deploy_path' : env.deploy_path})
    # extract zip file
    run('unzip %(project_directory)s/%(project_name)s/%(release)s.zip -d %(deploy_path)s' % {'deploy_path': env.deploy_path, 'release': env.release, 'project_directory' : env.project_directory, 'project_name' : env.project_name})
    print 'git master branch extracted in %(deploy_path)s' % {'deploy_path': env.deploy_path}
	# delete zip file
    local('rm %(release)s.zip' % {'release': env.release})

def _install_requirements():
    "Install the required packages from the requirements file using PIP" 
    require('deploy_path', provided_by = [production])
    
    print 'checking requirements from %(deploy_path)s/requirements.txt' % {'deploy_path': env.deploy_path}
    run('cd %(deploy_path)s; . %(virtualenv)s/bin/activate; pip install -r ./requirements.txt' % {'virtualenv': env.virtualenv, 'deploy_path': env.deploy_path})
    
def _update_settings():
    "Move the production settings config file"
    require('settings_path', provided_by = [production])
    require('deploy_path', provided_by = [production])
    require('www_user', provided_by = [production])
    
    # Go to local-settings, move settings.py of production to deploy_path as local.py
    print 'moving production settings to %(deploy_path)s/settings as local.py' % {'deploy_path': env.deploy_path}
    sudo('cd %(settings_path)s; cp production.py %(deploy_path)s/settings/local.py' % {'settings_path': env.settings_path, 'deploy_path': env.deploy_path})
    sudo('chown -R %(www_user)s:%(www_user)s %(deploy_path)s' % {'www_user': env.www_user, 'deploy_path': env.deploy_path})
   
def _create_database_schema():
    "Create the database tables for all apps in INSTALLED_APPS whose tables have not already been created"
    require('deploy_path', provided_by = [production])
    
    run('cd %(deploy_path)s/; . %(virtualenv)s/bin/activate; python manage.py syncdb --noinput --settings=settings.local' % {'deploy_path': env.deploy_path, 'virtualenv': env.virtualenv})

def _reload_apache():
    "Reload the apache server"
    sudo('apache2ctl restart')
