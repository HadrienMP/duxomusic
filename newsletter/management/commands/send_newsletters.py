__author__ = 'hadrien'
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from newsletter.models import *


_SENDER = settings.DEFAULT_FROM_EMAIL


class Command(BaseCommand):
    help = 'Sends all the newsletters that are supposed to be sent'

    def handle(self, *args, **options):
        newsletters = Mail.objects.filter(date_envoi__lte=timezone.now(), draft=False, sent=False)

        to_send = list()
        for newsletter in newsletters:
            subject, from_email = newsletter.sujet, _SENDER
            text_content = render_to_string('mail/newsletter.txt', {'corps': newsletter.corps})
            html_content = render_to_string('mail/newsletter.html', {'corps': newsletter.corps})

            for person in newsletter.list.subscribers.all():
                msg = EmailMultiAlternatives(subject, text_content, from_email, [person.email])
                msg.attach_alternative(html_content, "text/html")
                to_send.append(msg)

        print len(to_send)
        connection = mail.get_connection()
        connection.send_messages(to_send)