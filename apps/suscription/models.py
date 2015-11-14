# coding:utf-8
from django.db import models

from commons.models import CommonModel


class Suscriber(CommonModel):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )

    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email
