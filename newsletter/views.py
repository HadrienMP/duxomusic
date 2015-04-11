# -*- coding: utf-8 -*-
from __future__ import division

import csv

from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render

from .forms import *
from .models import *
import nm_msgs


_NEWSLETTER_DIR = os.path.abspath(os.path.dirname(__file__))


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            person = form.save()
            person.lists = List.objects.all()
            person.save()
            nm_msgs.success(request,
                            message=u"Merci pour ton inscription " + person.nom + " !",
                            namespace="newsletter")

        else:
            # Save the form to be able to display the errors and the sent values on the home page
            # and still prevent the double submit problem
            request.session['newsletter_form'] = form

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def read(request):
    form = ReadForm(request.GET)
    if form.is_valid():

        mail = Mail.objects.get(pk=form.cleaned_data['mail_id'])
        person = Person.objects.get(pk=form.cleaned_data['person_id'])

        if mail and person:
            mail.readers.add(person)
            mail.save()

    image_data = open(_NEWSLETTER_DIR + "/static/img/placeholder.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def stats(request):
    data = {
        'open_rate_last': 0,
        'open_rate_average': 0,
        'ids': list(),
        'recipients': list(),
        'open_rates': list(),
        'readers': list(),
    }

    mails = Mail.objects.all()

    if mails.count() > 0:

        sum_open_rates = 0
        for mail in mails:
            sum_open_rates += mail.readers.count() / mail.recipients.count()

        data = {
            'open_rate_last': mails[0].readers.count() / mails[0].recipients.count() * 100,
            'open_rate_average': sum_open_rates / len(mails) * 100,
            'ids': list(),
            'recipients': list(),
            'open_rates': list(),
            'readers': list(),
        }

        for mail in mails[:10]:
            data['ids'].append('#' + str(mail.pk))
            data['recipients'].append(mail.recipients.count())
            data['readers'].append(mail.readers.count())
            data['open_rates'].append(mail.readers.count() / mail.recipients.count() * 100)

    return render(request, 'stats.html', data)


def mass_import(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded = request.FILES['file']
            file_reader = csv.DictReader(uploaded, delimiter=',', quotechar='"')
            to_create = list()
            rejected = list()
            for row in file_reader:
                if Person.objects.filter(email=row['email']).count() == 0:
                    person = Person()
                    person.email = row['email']
                    person.nom = row['name']
                    person.date_creation = datetime.datetime.strptime(row['sign_up'], "%Y-%m-%d %H:%M:%S")
                    to_create.append(person)
                else:
                    rejected.append(row)

            Person.objects.bulk_create(to_create)

            if len(rejected) != 0:
                nm_msgs.warning(request,
                                message=u"Les lignes suivantes existent déjà : " + str(rejected),
                                namespace="newsletter")
            nm_msgs.success(request,
                            message=u"L'import a été effectué avec succès",
                            namespace="newsletter")
            return HttpResponseRedirect('')
    else:
        form = ImportForm()

    return render(request, 'import.html', {
        'form': form
    })