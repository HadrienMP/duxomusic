__author__ = 'hadrien'
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class NewsletterToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu('newsletter-app', _('Newsletter'))
        menu.add_sideframe_item(_('Stats'), url=reverse('newsletter:stats'))
        menu.add_sideframe_item(_('Import'), url=reverse('newsletter:import'))