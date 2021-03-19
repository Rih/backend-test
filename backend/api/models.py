# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import random

# Model states
MODEL_STATES = {
    'ACTIVE': '1',
    'DELETE': '-1'
}

STATES = [
    (MODEL_STATES['DELETE'], 'Inactivo'),
    (MODEL_STATES['ACTIVE'], 'Activo'),
]


class Apimodel(models.Model):
    ACTIVE = MODEL_STATES['ACTIVE']
    DELETE = MODEL_STATES['DELETE']
    STATES = [
        (DELETE, 'Inactivo'),
        (ACTIVE, 'Activo'),
    ]
    estado = models.CharField(
        max_length=10,
        choices=STATES,
        default=ACTIVE
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    last_modified = models.DateTimeField(
        null=True,
        auto_now=True
    )

    class Meta:
        abstract = True


def sitio_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/sitio_<id>/<filename>
    return 'site_{0}/{1}'.format(instance.user.pk, filename)


def kml_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<type>/<filename>_<id>/<filename>
    return '{0}/{1}_{2}/{3}'.format(
        instance.type,
        instance.filename,
        round(random.randint(0, 999999)),
        filename
    )

