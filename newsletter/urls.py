# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^subscribe$', views.subscribe, name="subscribe"),
    url(r'^read$', views.read, name="read"),
    url(r'^stats$', views.stats, name="stats"),
    url(r'^import$', views.mass_import, name="import"),
)
