# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^subscribe$', views.subscribe, name="subscribe"),
    url(r'^read$', views.read, name="read"),
)
