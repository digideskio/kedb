
from django import http
from django import shortcuts
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import ContextMixin, View

class EventHandlerView(ContextMixin, View):

    def get(self, request, *args, **kwargs):
        return 'OK'
