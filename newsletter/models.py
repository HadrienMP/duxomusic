# -*- coding: utf-8 -*-
from django.db import models
from uuidfield import UUIDField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from cms.models.pluginmodel import CMSPlugin


class Person(models.Model):
    """A person in the mailing list (a subscriber)"""

    email = models.EmailField(max_length=254, unique=True)
    prenom = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_desinscription = models.DateTimeField(blank=True, null=True)
    opt_in = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    token = UUIDField(auto=True)

    def __unicode__(self):
        return '{0} : {1}'.format(self.prenom, self.email)

    class Meta:
        verbose_name = _('personne')
        verbose_name_plural = _('personnes')


class List(models.Model):
    """A list of personn subscribing to a newsletter"""

    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    subscribers = models.ManyToManyField(Person, blank=True, related_name='lists')

    def __unicode__(self):
        return self.nom


class Mail(models.Model):
    """A mail that is sent to all or a subset of the subscribers of a list or lists"""

    sujet = models.CharField(max_length=255, unique=True)
    corps = models.TextField(help_text=_("Use {prenom} in the text to insert the recipient's first name."))
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_envoi = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    sent = models.BooleanField(default=False)

    list = models.ForeignKey(List, related_name='mails')
    recipients = models.ManyToManyField(Person, blank=True)
    readers = models.ManyToManyField(Person, related_name='read_mails', blank=True)

    def __unicode__(self):
        if self.sent:
            definition = '"{0}" - Sent to {1} persons (around {2})'
        else:
            definition = '"{0}"'
            if self.draft:
                definition += " - Brouillon"
        return definition.format(self.sujet, len(self.recipients.all()),
                                 self.date_envoi.strftime('%H:%M the %d/%m/%Y'))

    class Meta:
        ordering = ['-date_envoi']


class Link(models.Model):
    """A link in a mail we wish to track"""

    url = models.URLField()

    mail = models.ForeignKey(Mail, related_name='links')
    clickers = models.ManyToManyField(Person, blank=True)


class NewsletterPluginModel(CMSPlugin):
    """The model that allows to chose to which list you want your subscribers to subscribe to"""
    list = models.ForeignKey(List)
    call_to_action = models.TextField('Call To Action', null=True, blank=True)
