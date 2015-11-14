# coding:utf-8
from django.contrib import admin

from suscription.models import Suscriber


class SuscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'enabled', 'created_at',)
    list_display_links = ('email', 'created_at',)
    list_editable = ('enabled',)
    list_filter = ('enabled', 'created_at',)
    search_fields = ('email',)


admin.site.register(Suscriber, SuscriberAdmin)
