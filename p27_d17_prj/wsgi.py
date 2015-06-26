"""
WSGI config for p27_d17 project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#
# BASE_DIR is useless as it is one directory above the one with manage.py
PROJECT_DIR = os.path.join(os.path.dirname(__file__))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
# put apps on first part of path so we can leave off apps. when
# importing an app
sys.path.insert(0, APPS_DIR)
print sys.path
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "p27_d17.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p27_d17_prj.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
