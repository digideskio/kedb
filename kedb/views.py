
import json
from django import http
from django import shortcuts
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import ContextMixin, View
from django.http import HttpResponse

import logging

log = logging.getLogger('kedb.views')

from kedb.models import KnownError

"""
payload from sensu handler

{
  "timestamp":"2014-05-19T16:35:31.094581+0200",
  "level":"info",
  "message":"handler output",
  "handler":{
    "type":"pipe",
    "command":"/etc/sensu/handlers/sccd.py",
    "name":"sccd"
  },
  "output":"{
    'event': {
      'action': 'create', 
      'client': {
        'name': 'sensu1.state.newt.cz', 
        'subscriptions': ['local-salt-minion', ..., 'local-common'],
        'timestamp': 1400510124,
        'system': 'state_base',
        'graphite_name': 'sensu1_state_newt_cz',
        'address': '10.0.2.15'
      },
      'check': {
        'status': 2,
        'executed': 1400510130,
        'name': 'remote_keystone_api',
        'handlers': ['default'],
        'issued': 1400510130,
        'interval': 60,
        'command': 'PATH=$PATH:/srv/sensu/checks python check_http_json.py -H 10.0.102.20:5000 -p v2.0',
        'occurrences': 1,
        'subscribers': ['remote-network'],
        'duration': 0.012999999999999999,
        'output': \"python: can't open file 'check_http_json.py': [Errno 2] No such file or directory\\n\", 
        'history': ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
      },
      'occurrences': 828
    }
  }"
}

{"event": {"action": "create", "client": {"name": "sensu1.state.newt.cz", "subscriptions": ["local-salt-minion", "sensu1-state-newt-cz", "local-common"],
 "timestamp": 1400743301, "system": "state_base", "graphite_name": "sensu1_state_newt_cz", "address": "10.0.2.15"}, 
 "check": {"customer": "customer01", "status": 2, "executed": 1400743305, "name": "remote_keystone_api", "handlers": ["default"], "issued": 1400743305, "interval": 60, 
 "command": "PATH=$PATH:/srv/sensu/checks python check_http_json.py -H 10.0.102.20:5000 -p v2.0", "occurrences": 1, "subscribers": ["remote-network"], 
 "duration": 0.021999999999999999, "output": "python: can't open file 'check_http_json.py': [Errno 2] No such file or directory\n", 
 "history": ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"], "asset": "asset01"}, 
 "occurrences": 2485}}
"""

def _find_by_event(check, output):

        error = KnownError.find_by_event(check, output)
        event = {}

        if error == None:
            event['known_error'] = False
            event['error_name'] = 'Unknown error'
        else:
            event['known_error'] = True
            event['error_name'] = error.name
            event['level'] = error.level
            event['severity'] = error.severity

        return event

class EventHandlerView(ContextMixin, View):

    def post(self, request, *args, **kwargs):
        event = json.loads(request.raw_post_data)['event']
        
        event.update(_find_by_event(event['check']['name'], event['check']['output']))

        return HttpResponse(json.dumps(event))

class EventDetailView(ContextMixin, View):

    def post(self, request, *args, **kwargs):
        event = json.loads(request.raw_post_data)['event']

        event.update(_find_by_event(event['check'], event['output']))

        return HttpResponse(json.dumps(event))

class EventListView(ContextMixin, View):

    def get(self, request, *args, **kwargs):
      return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        events = json.loads(request.raw_post_data)['events']
        output = []

        for event in events:

            event.update(_find_by_event(event['check'], event['output']))
            output.append(event)

        return HttpResponse(json.dumps(output))
