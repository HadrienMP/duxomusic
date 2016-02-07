# -*-coding:utf-8-*-
from django.db import models
from filer.fields.image import FilerImageField
from colorfield.fields import ColorField

    
class Background(models.Model):
    active = models.BooleanField("Actif", default=False, blank=True)
    color = ColorField("Couleur de fond", default="000000")
    no_background_split = models.IntegerField("Taille à partir de laquelle on n'affiche plus l'image de fond", default=480)

    def __unicode__(self):
        active_str = u"O" if self.active else u"X"
        return active_str + u" Background n°" + unicode(self.pk)
        
        
class ImageWrapper(models.Model):
    image = FilerImageField()
    background = models.ForeignKey(Background, related_name='images')

    def __unicode__(self):
        return unicode(self.image)
        