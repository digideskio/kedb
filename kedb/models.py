
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
    ("l1", u"Level 1"),
    ("l2", u"Level 2"),
)

SEVERITY_CHOICES = (
    ("int", u"Internal"),
    ("999", u"SLA 99.9"),
    ("9999", u"SLA 99.99"),
)

OWNERSHIP_CHOICES = (
    ("cloud", u"Cloud"),
    ("network", u"Network"),
    ("hardware", u"Hardware"),
)

ENGINE_CHOICES = (
    ("salt", u"Salt call"),
    ("jenkins", u"Jenkins job"),
    ("misc", u"Misc"),
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
        instances = KnownError.objects.filter(check=check)
        final_instance = None
        for instance in instances:
            if len(re.findall(instance.output_pattern, output)) > 0:
                final_instance = instance
        return final_instance

    class Meta:
        verbose_name = _("known error")
        verbose_name_plural = _("known errors")

class Workaround(models.Model):
    known_error = models.ForeignKey(KnownError, verbose_name=_('known error'), related_name='workarounds')
    description = models.TextField(verbose_name=_('description'), blank=True)
    temporary = models.BooleanField(max_length=255, verbose_name=_('temporary'))
    engine = models.CharField(max_length=255, verbose_name=_('engine'), default='salt', choices=ENGINE_CHOICES)
    action = models.TextField(verbose_name=_('description'), blank=True)

    @property
    def error_detail(self):
        return self.known_error

    class Meta:
        verbose_name = _("workaround")
        verbose_name_plural = _("workarounds")
