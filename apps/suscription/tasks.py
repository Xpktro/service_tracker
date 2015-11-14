# coding:utf-8
from __future__ import absolute_import

import requests
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string

from services.models import Service, ServiceStatus
from suscription.models import Suscriber


@shared_task
def send_mass_email():
    to = []
    suscribers = Suscriber.objects.filter(enabled=True)
    service_queryset = Service.objects.all()
    status_queryset = ServiceStatus.objects.all()[:4]
    suscribers_count = suscribers.count()
    email_content = render_to_string(
        'email.html',
        {'services': service_queryset, 'statuses': status_queryset}
    )

    for suscriber in suscribers.iterator():
        to.append(suscriber.email)
        if len(to) >= settings.MAILGUN_BATCH_SEND or len(to) == suscribers_count:
            requests.post(
                '%s/messages' % settings.MAILGUN_BASE_URL,
                auth=('api', settings.MAILGUN_API_KEY),
                data={
                    'from': 'Service Tracker <service@tracker.com>',
                    'to': to,
                    'subject': 'Service Tracker Status Update',
                    'html': email_content,
                    'recipient-variables': '{}'
                }
            )
            to = []
            suscribers_count -= settings.MAILGUN_BATCH_SEND

    return True
