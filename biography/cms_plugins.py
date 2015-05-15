from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *


class BiographyPlugin(CMSPluginBase):
    model = Biography
    module = _("HadrienMP")
    name = _('Biography')
    render_template = "biography.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(BiographyPlugin)
