from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from contact.models import *


class ContactItemAdmin(admin.TabularInline):
    model = ContactItem


class ContactPlugin(CMSPluginBase): 
    model = Contact
    module = _("HadrienMP")
    name = _('Contact Plugin')
    render_template = "contact_plugin.html"
    
    inlines = [ContactItemAdmin]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ContactPlugin)
