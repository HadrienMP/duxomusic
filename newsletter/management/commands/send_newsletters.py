__author__ = 'hadrien'
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from newsletter.models import *


_SENDER = settings.DEFAULT_FROM_EMAIL
_READ_URL = settings.BASE_URL + '/newsletter/read?person_id={0}&amp;mail_id={1}'


class Command(BaseCommand):
    help = 'Sends all the newsletters that are supposed to be sent'

    def handle(self, *args, **options):
        newsletters = Mail.objects.filter(date_envoi__lte=timezone.now(), draft=False, sent=False)

        to_send = list()
        for newsletter in newsletters:
            subject, from_email = newsletter.sujet, _SENDER

            for person in newsletter.list.subscribers.all():
                data = {
                    'corps': newsletter.corps.format(nom=person.nom),
                    'read_track_url': _READ_URL.format(person.pk, newsletter.pk),
                    'unsubscribe_url': '',
                    'change_info_url': ''
                }
                text_content = render_to_string('mail/newsletter.txt', data)
                html_content = render_to_string('mail/newsletter.html', data)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [person.email])
                msg.attach_alternative(html_content, "text/html")
                to_send.append(msg)

        print len(to_send)
        connection = mail.get_connection()
        connection.send_messages(to_send)

        for newsletter in newsletters:
            newsletter.sent = True
            newsletter.date_envoi = timezone.now()
            newsletter.save()