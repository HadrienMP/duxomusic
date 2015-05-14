from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from raw_html.models import *


class RawHtmlPlugin(CMSPluginBase):
    model = RawHtml
    module = _("HadrienMP")
    name = _('Html Brut')
    render_template = "raw_html.html" 
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(RawHtmlPlugin)
