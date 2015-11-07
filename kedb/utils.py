
import logging
import re

from django.conf import settings
from kedb.models import KnownError
from kedb.serialisers import KnownErrorSerializer

log = logging.getLogger('kedb.utils')


def _find_by_event(check, output):
    """core method which tries find known error by check and output
    """

    instances = KnownError.objects.filter(check__iregex=r"{0}*".format(check))

    final_instance = None

    for instance in instances:
        try:
            if len(re.findall(instance.output_pattern, output)) > 0:
                final_instance = instance
        except Exception as e:
            log.error(e)

    # create known error for unknown events
    if not final_instance and getattr(
            settings, 'KEDB_ERRORS_AUTOCREATE', False):

        # trim if needit
        try:
            re.sub(r'^(.{254}).*$', '', output)
        except:
            pass

        final_instance, created = KnownError.objects.get_or_create(
            name='Error - %s' % check,
            check=check,
            description=output,
            defaults={'output_pattern': output[:255]
                      if len(output) > 255 else output})
    return final_instance


def find_by_event(check, output=None):

    error = _find_by_event(check['name'], output or check["output"])
    event = {}

    if error is None:
        event['known_error'] = False
        event['error_name'] = 'Unknown error'
    else:
        event['known_error'] = True
        serializer = KnownErrorSerializer(error)
        event['error_name'] = error.name
        event['description'] = error.description
        event['level'] = error.level
        event['severity'] = error.severity
        event['error_id'] = error.id
        event['workarounds'] = serializer.data.get("workarounds")
    return event
