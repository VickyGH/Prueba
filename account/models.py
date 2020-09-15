from __future__ import unicode_literals
import os
from django.db import models

from core.helpers.model import TimeStamp

Type_Choice = (
    ('Normal', u'Normal'),
    ('Plata', u'Plata'),
    ('Oro', u'Oro'),
    ('Platino', u'Platino'),
)


def get_image(instance, filename):
    return os.path.join('image', filename)


class Client(TimeStamp):
    name = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to=get_image, blank=True, null=True)
    address = models.TextField()
    type = models.CharField(max_length=100, blank=True,choices=Type_Choice, default='Normal')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
