from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from colorfield.fields import ColorField


class Biography(CMSPlugin):
    photo = FilerImageField(related_name="photo")
    hover_photo = FilerImageField(related_name="hover_photo", blank=True, null=True)
    description = HTMLField()

