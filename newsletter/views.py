# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from .forms import NewsletterForm
import nm_msgs


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            nm_msgs.success(request,
                            message=u"Merci pour ton inscription " + form.cleaned_data['nom'] + " !",
                            namespace="newsletter")

        else:
            # Save the form to be able to display the errors and the sent values on the home page
            # and still prevent the double submit problem
            request.session['newsletter_form'] = form

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
