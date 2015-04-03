from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import *
from .forms import *


class NewsletterPlugin(CMSPluginBase):
    model = NewsletterPluginModel
    module = _("HadrienMP")
    name = _('Subscribe Form')
    render_template = "subscribe_form.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['form'] = NewsletterForm()

        # If there is a form in session (put there by the subscribe view)
        # we put it in the context in order to be able to use form.errors
        # in the template

        request = context['request']
        if 'newsletter_form' in request.session:
            context['form'] = request.session['newsletter_form']
            del request.session['newsletter_form']

        return context

plugin_pool.register_plugin(NewsletterPlugin)
