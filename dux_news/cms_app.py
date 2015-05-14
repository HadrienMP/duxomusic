__author__ = 'hadrien'
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class DuxNewsApp(CMSApp):
    name = _("Dux News App")
    urls = ["dux_news.urls"]
    app_name = 'dux_news'


apphook_pool.register(DuxNewsApp)