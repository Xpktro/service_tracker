# coding:utf-8
from django.db import models
from model_utils import FieldTracker

from commons.models import CommonModel
import constants


class MassEmailOnChangeMixin(object):

    def save(self, *args, **kwargs):
        if self.tracker.changed():
            from suscription.tasks import send_mass_email
            send_mass_email.delay()
        return super(MassEmailOnChangeMixin, self).save(*args, **kwargs)


class Service(MassEmailOnChangeMixin, CommonModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    status = models.SmallIntegerField(
        choices=constants.SERVICE_STATUS_CHOICES,
        blank=False,
        null=False
    )

    tracker = FieldTracker()

    def __unicode__(self):
        return self.name


class ServiceStatus(MassEmailOnChangeMixin, CommonModel):
    service = models.ForeignKey(
        Service,
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    text = models.TextField(
        blank=False
    )

    tracker = FieldTracker()

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = u'Service statuses'
        ordering = ('-created_at',)
