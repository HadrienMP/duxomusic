# -*- coding:utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.
class TitleDivider(CMSPlugin):
    title = models.CharField("Titre à afficher", max_length=100)
