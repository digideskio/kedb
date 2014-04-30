
import os

from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.models import User, Group

from kedb.models import KnownError
from rest_framework import viewsets, routers

admin.autodiscover()

class KnownErrorViewSet(viewsets.ModelViewSet):
    model = KnownError

router_api_v1 = routers.DefaultRouter()
router_api_v1.register(r'known-errors', KnownErrorViewSet)

urlpatterns = patterns('',
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router_api_v1.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + staticfiles_urlpatterns()
