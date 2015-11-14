# coding:utf-8
from django import template

from services.constants import SERVICE_STATUS_CLASSES

register = template.Library()


@register.filter
def status_class(status):
    return SERVICE_STATUS_CLASSES[status]