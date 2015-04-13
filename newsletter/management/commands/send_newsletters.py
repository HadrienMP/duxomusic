__author__ = 'hadrien'
from django.core.management.base import BaseCommand
from django.utils import timezone

from newsletter.service import *


_SENDER = settings.DEFAULT_FROM_EMAIL
_READ_URL = settings.BASE_URL + '/newsletter/read?person_id={0}&amp;mail_id={1}'


class Command(BaseCommand):
    help = 'Sends all the newsletters that are supposed to be sent'

    def handle(self, *args, **options):
        newsletters = Mail.objects.filter(date_envoi__lte=timezone.now(), draft=False, sent=False)

        to_send = list()

        for newsletter in newsletters:
            for person in newsletter.list.subscribers.filter(active=True):
                to_send.append(prepare_newsletter(person, newsletter))

        print len(to_send)
        connection = mail.get_connection()
        connection.send_messages(to_send)

        for newsletter in newsletters:
            newsletter.sent = True
            newsletter.date_envoi = timezone.now()
            # Save the recipients to calculate an acurate in time open rate
            newsletter.recipients = newsletter.list.subscribers.filter(active=True)
            newsletter.save()