from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from title_divider.models import *


class TitleDividerPlugin(CMSPluginBase):
    model = TitleDivider
    module = _("HadrienMP")
    name = _('Title Divider')
    render_template = "title_divider_plugin.html" 
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TitleDividerPlugin)
