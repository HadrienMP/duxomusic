import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'duxomusic.settings'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
