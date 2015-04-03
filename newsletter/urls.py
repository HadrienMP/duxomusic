# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, patterns, include
from . import views

urlpatterns = patterns('',
    url(r'^subscribe$', views.subscribe, name="subscribe"),
)
