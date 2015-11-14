# coding:utf-8
from __future__ import absolute_import

import os
import sys
from celery import Celery

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PATHS = [os.path.realpath(os.path.join(BASE_DIR, 'apps'))]
for path in PATHS:
    sys.path.insert(0, path)
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

from django.conf import settings  # noqa

app = Celery('mailer', broker='amqp://', backend='amqp://')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
