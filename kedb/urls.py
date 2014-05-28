
import os
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from kedb.models import KnownError, Workaround
from kedb.views import EventHandlerView, EventListView, EventDetailView
from kedb.serialisers import KnownErrorSerializer, WorkaroundSerializer

admin.autodiscover()

class KnownErrorViewSet(viewsets.ModelViewSet):
    model = KnownError
    serializer_class = KnownErrorSerializer

class WorkaroundViewSet(viewsets.ModelViewSet):
    model = Workaround
    serializer_class = WorkaroundSerializer

router_api_v1 = routers.DefaultRouter()
router_api_v1.register(r'known-errors', KnownErrorViewSet)
router_api_v1.register(r'workarounds', WorkaroundViewSet)

urlpatterns = patterns('',
    url(r'^api/events/', csrf_exempt(EventListView.as_view()), name='event_list'),
    url(r'^api/events/detail/', csrf_exempt(EventDetailView.as_view()), name='event_detail'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router_api_v1.urls)),
    url(r'^handle/', csrf_exempt(EventHandlerView.as_view()), name='handle_event'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
