from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save

from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin
from taggit_autosuggest.managers import TaggableManager


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
    tags = TaggableManager(blank=True, related_name='dux_news_tags')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('dux_news:sound_detail', kwargs=kwargs)

@receiver(pre_save, sender=Sound)
def after_sound_save(sender, instance, *args, **kwargs):
    if '<iframe' in instance.sound:
        instance.sound = '<div class="iframe-video-wrapper">' + instance.sound + '</div>'

class NewSound(CMSPlugin):
    sound = models.ForeignKey(Sound)