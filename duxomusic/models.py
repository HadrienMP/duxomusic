# -*-coding:utf-8-*-
from django.db import models
from filer.fields.image import FilerImageField

    
class Background(models.Model):
    active = models.BooleanField("Actif", default=False, blank=True)

    def __unicode__(self):
        active_str = u"O" if self.active else u"X"
        return active_str + u" Background n°" + unicode(self.pk)
        
        
class ImageWrapper(models.Model):
    image = FilerImageField()
    background = models.ForeignKey(Background, related_name='images')

    def __unicode__(self):
        return unicode(self.image)
        