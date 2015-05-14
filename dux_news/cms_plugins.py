from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *


class NewSoundPlugin(CMSPluginBase):
    model = NewSound
    module = _("HadrienMP")
    name = _('New Sound')
    render_template = "dux_news/sound_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(NewSoundPlugin)
