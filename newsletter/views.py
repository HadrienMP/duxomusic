# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
import os

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

        mail = Mail.objects.get(pk=form.cleaned_data('mail_id'))
        person = Person.objects.get(pk=form.cleaned_data('person_id'))

        if mail and person:
            mail.readers.add(person)
            mail.save()

    image_data = open(_NEWSLETTER_DIR + "/static/img/placeholder.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")