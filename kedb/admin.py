# -*- coding: UTF-8 -*-

from django.contrib import admin, messages
from django.db.models import Q
from django.http import HttpResponseRedirect

from kedb.models import KnownError

class KnownErrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'check', 'output_pattern')

admin.site.register(KnownError, KnownErrorAdmin)
