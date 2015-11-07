
import json
import logging

from django.http import HttpResponse
from django.views.generic.base import ContextMixin, View
from kedb.utils import find_by_event

log = logging.getLogger('kedb.views')


class EventHandlerView(ContextMixin, View):

    def post(self, request, *args, **kwargs):
        event = json.loads(request.body)['event']

        event.update(
            find_by_event(event['check']['name'], event['check']['output']))

        return HttpResponse(json.dumps(event))


class EventDetailView(ContextMixin, View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        event = json.loads(request.body)['event']

        event.update(find_by_event(event['check']['name']))

        return HttpResponse(json.dumps(event))


class EventListView(ContextMixin, View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        output = []

        try:
            events = json.loads(request.body)['events']
            for event in events:
                event.update(find_by_event(event["check"]))
                output.append(event)
        except Exception as e:
            raise e
            log.error(e)

        return HttpResponse(json.dumps(output))
