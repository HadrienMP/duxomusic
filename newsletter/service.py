# -*- coding: utf-8 -*-
__author__ = 'hadrien'
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from .models import *


_SENDER = settings.DEFAULT_FROM_EMAIL
_READ_URL = settings.BASE_URL + '/newsletter/read?person_id={0}&amp;mail_id={1}'
_ACTIVATION_URL = settings.BASE_URL + '/newsletter/user/activate?token={0}'
_UNSUBSCRIBE_URL = settings.BASE_URL + '/newsletter/user/unsubscribe?token={0}'
_EDIT_URL = settings.BASE_URL + '/newsletter/user/edit?token={0}'


def send_confirmation_mail(person):
    if not isinstance(person, Person):
        raise TypeError("Type Person expected")

    data = _confirmation_mail_data(person)
    _send_mail(person, 'Confirmes ton inscription à la newsletter', data, 'confirmation')


def _confirmation_mail_data(person):
    data = {
        'nom': person.nom,
        'activation_link': _ACTIVATION_URL.format(person.token),
    }
    return data


def _send_mail(person, subject, data, template_name):
    to_send = list()
    text_content = render_to_string('mail/{0}.txt'.format(template_name), data)
    html_content = render_to_string('mail/{0}.html'.format(template_name), data)
    msg = EmailMultiAlternatives(subject, text_content, _SENDER, [person.email])
    msg.attach_alternative(html_content, "text/html")
    to_send.append(msg)
    connection = mail.get_connection()
    connection.send_messages(to_send)


def prepare_newsletter(person, newsletter):
    data = {
        'corps': newsletter.corps.format(nom=person.nom),
        'read_track_url': _READ_URL.format(person.pk, newsletter.pk),
        'unsubscribe_url': _UNSUBSCRIBE_URL.format(person.token),
        'change_info_url': _EDIT_URL.format(person.token)
    }
    text_content = render_to_string('mail/newsletter.txt', data)
    html_content = render_to_string('mail/newsletter.html', data)
    msg = EmailMultiAlternatives(newsletter.sujet, text_content, _SENDER, [person.email])
    msg.attach_alternative(html_content, "text/html")

    return msg