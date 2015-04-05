# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect

from .forms import NewsletterForm
from .models import *
import nm_msgs


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
