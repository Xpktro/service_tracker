# coding:utf-8
from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=u'Created at',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name=u'Last update at',
        auto_now=True
    )

    class Meta:
        abstract = True
