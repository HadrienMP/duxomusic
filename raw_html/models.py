from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

class RawHtml(CMSPlugin):
    html = models.TextField(max_length=500)
