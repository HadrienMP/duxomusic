# -*- coding: utf-8 -*-
from __future__ import division

import csv
import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .forms import *
from newsletter.service import *
import nm_msgs


_NEWSLETTER_DIR = os.path.abspath(os.path.dirname(__file__))


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            person = form.save()
            person.lists = List.objects.all()
            person.save()

            # Sends the confirmation message
            send_confirmation_mail(person)

            nm_msgs.success(request,
                            message=u"Merci pour ton inscription " + person.prenom + " !",
                            namespace="newsletter")

        else:
            # Save the form to be able to display the errors and the sent values on the home page
            # and still prevent the double submit problem
            request.session['newsletter_form'] = form

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def read(request):
    form = ReadForm(request.GET)
    if form.is_valid():

        newsletter = Mail.objects.get(pk=form.cleaned_data['mail_id'])
        person = Person.objects.get(pk=form.cleaned_data['person_id'])

        if newsletter and person:
            newsletter.readers.add(person)
            newsletter.save()

    image_data = open(_NEWSLETTER_DIR + "/static/img/placeholder.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def activate(request):
    form = ActivationForm(request.GET)
    if form.is_valid():

        person = Person.objects.get(token=form.cleaned_data['token'])

        if person:
            person.active = True
            person.opt_in = True
            person.save()

    return render(request, 'app/confirmation.html')


def unsubscribe(request):
    form = ActivationForm(request.GET)
    if form.is_valid():

        person = Person.objects.get(token=form.cleaned_data['token'])

        if person:
            person.active = False
            person.date_desinscription = timezone.now()
            person.save()

    return render(request, 'app/unsubscribe.html')


def edit_user(request):
    newsletter_form = None
    person = None

    # Get the person that correspond to the token
    form = ActivationForm(request.GET or None)
    if form.is_valid():
        person = get_object_or_404(Person, token=form.cleaned_data['token'])
        newsletter_form = NewsletterForm(instance=person)

    if request.POST:
        newsletter_form = NewsletterForm(request.POST, instance=person)
        if newsletter_form.is_valid():
            newsletter_form.save()
            nm_msgs.success(request,
                            message=u"Modification terminée.",
                            namespace="newsletter")
            return redirect(request.get_full_path())

    if newsletter_form:
        return render(request, 'app/edit.html', {'form': newsletter_form, 'action': request.get_full_path()})
    else:
        return redirect('/')


@login_required
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

    return render(request, 'newsletter_admin/stats.html', data)


@login_required
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
                    person.prenom = row['name']
                    person.date_creation = datetime.datetime.strptime(row['sign_up'], "%Y-%m-%d %H:%M:%S")
                    person.active = True
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

    return render(request, 'newsletter_admin/import.html', {
        'form': form
    })