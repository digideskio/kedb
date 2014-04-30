import os
import re
from datetime import datetime
from logging import getLogger

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class KnownError(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True)

    check = models.CharField(max_length=255, verbose_name=_('sensu check'),)
    output_pattern = models.CharField(max_length=255, verbose_name=_('output pattern'),)

    level = models.CharField(max_length=55, verbose_name=_('level'), default='L1')
    severity = models.CharField(max_length=55, verbose_name=_('severity'), default='medium')

    class Meta:
        verbose_name = _("known error")
        verbose_name_plural = _("known errors")
