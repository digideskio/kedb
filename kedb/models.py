import os
import re
from datetime import datetime
from logging import getLogger

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

LEVEL_CHOICES = (
    ("level1", u"level 1"),
    ("level2", u"level 2"),
)

SEVERITY_CHOICES = (
    ("low", u"low"),
    ("medium", u"medium"),
    ("high", u"high"),
)

OWNERSHIP_CHOICES = (
    ("cloudlab", u"Cloudlab"),
    ("network", u"network"),
)

class KnownError(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    check = models.CharField(max_length=255, verbose_name=_('sensu check'),)
    output_pattern = models.CharField(max_length=255, verbose_name=_('output pattern'))
    level = models.CharField(max_length=55, verbose_name=_('level'), default='level1', choices=LEVEL_CHOICES)
    severity = models.CharField(max_length=55, verbose_name=_('severity'), default='medium', choices=SEVERITY_CHOICES)
    ownership = models.CharField(max_length=55, verbose_name=_('ownership'), default='cloudlab', choices=OWNERSHIP_CHOICES)

    @classmethod
    def find_by_event(cls, check, output):
        lookup = {
            'a': 'b'
        }
        try:
            instance = KnownError.objects.all()[0]
        except:
            instance = None
        return instance

    class Meta:
        verbose_name = _("known error")
        verbose_name_plural = _("known errors")

class Workaround(models.Model):
    known_error = models.ForeignKey(KnownError, verbose_name=_('known error'), related_name='workarounds')
    description = models.TextField(verbose_name=_('description'), blank=True)
    temporary = models.BooleanField(max_length=255, verbose_name=_('temporary'))

    class Meta:
        verbose_name = _("workaround")
        verbose_name_plural = _("workarounds")
