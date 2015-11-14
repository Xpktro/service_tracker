# coding:utf-8
from commons.datastructures import Enumeration

SERVICE_STATUS_CHOICES = Enumeration([
    (0, 'UNKNOWN', u'Unknown'),
    (1, 'DOWN', u'Down'),
    (2, 'IN_MAINTENANCE', u'In Maintenance'),
    (3, 'UP', u'Up')
])

SERVICE_STATUS_CLASSES = [
    'active',
    'danger',
    'warning',
    'success'
]
