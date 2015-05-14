# -*- coding:utf-8 -*-
from django.db import models

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from colorfield.fields import ColorField
from djangocms_text_ckeditor.fields import HTMLField


class Contact(CMSPlugin):
    call_to_action = HTMLField(blank=True)

    def copy_relations(self, oldinstance):
        for item in oldinstance.items.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but 
            # standard Django way of copying a saved model instance 
            item.pk = None
            item.plugin = self
            item.save()


class ContactItem(models.Model):
    '''Une icone de contact'''

    icon = FilerImageField(null=True, blank=True, related_name="contact_icon",
                help_text="Modifiée automatiquement pour atteindre une taille de 100px x 100px. Si vous ne remplissez pas ce champ l'application tentera d'afficher l'icone Font-Awesome.")
    url = models.URLField("URL", null=True, blank=True)
    mail = models.EmailField("Email", max_length=254, null=True, blank=True)
    title = models.CharField("Titre",max_length=50, default='Contact', help_text="Affiché au survol de l'image représentant le contact")
    fa = models.CharField("Icone Font Awesome",max_length=50, null=True, blank=True, help_text="Ajoutez ici le nom d'une icône Font-Awesome")
    bgcolor = ColorField("Couleur de fond", null=True, blank=True, default="444444")

    plugin = models.ForeignKey(Contact, related_name="items")
    
