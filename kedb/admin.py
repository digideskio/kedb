# -*- coding: UTF-8 -*-

from django.contrib import admin, messages
from django.db.models import Q
from django.http import HttpResponseRedirect

from kedb.models import KnownError, Workaround

class WorkaroundInline(admin.TabularInline):
    model = Workaround
    extra = 5

class WorkaroundAdmin(admin.ModelAdmin):
    list_display = ('description', 'known_error', 'temporary')

admin.site.register(Workaround, WorkaroundAdmin)

class KnownErrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'check', 'output_pattern', 'severity')
    list_filter = ('check', 'severity', 'level')
    inlines = [WorkaroundInline,]

admin.site.register(KnownError, KnownErrorAdmin)
