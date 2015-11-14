# coding:utf-8

from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            _('User Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.auth.models.User',),
        ))

        self.children.append(modules.ModelList(
            _('Services'),
            column=1,
            collapsible=False,
            models=('services.*',),
        ))

        self.children.append(modules.ModelList(
            _('Suscriptions'),
            column=1,
            collapsible=False,
            models=('suscription.*',),
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))


