# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns(
    'dux_news',
    url(r'^(?P<slug>\w[-\w]*)$', sound_detail, name='sound_detail'),
)