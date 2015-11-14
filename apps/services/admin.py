# coding:utf-8
from django.contrib import admin

from services.models import ServiceStatus, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'updated_at',)
    list_display_links = ('name', 'updated_at')
    list_editable = ('status',)
    list_filter = ('status', 'updated_at',)


class ServiceStatusAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'created_at', 'updated_at',)
    list_display_links = list_display
    ordering = ('-created_at',)
    list_filter = ('service', 'created_at', 'updated_at',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceStatus, ServiceStatusAdmin)
