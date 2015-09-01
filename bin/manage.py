#!/usr/lib/django-helpdesk/bin/python

import sys
import os

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'kedb.settings'
    execute_from_command_line(sys.argv)
