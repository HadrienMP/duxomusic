from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin


class Sound(models.Model):
    sound = models.TextField(max_length=500)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_publication = models.DateTimeField(default=timezone.now)
    date_depublication = models.DateTimeField(blank=True, null=True)
    draft = models.BooleanField(default=True)
    description = HTMLField(blank=True)
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('dux_news:sound_detail', kwargs=kwargs)


class NewSound(CMSPlugin):
    sound = models.ForeignKey(Sound)