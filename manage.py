#!/usr/bin/env python
# manage.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# This is Django's COMMAND CENTER — your remote control.
# You'll use this file constantly via the Terminal.
#
# Common commands you'll type:
#   python3 manage.py runserver       → starts the web server
#   python3 manage.py makemigrations  → prepares database changes
#   python3 manage.py migrate         → applies database changes
#   python3 manage.py createsuperuser → creates an admin account
#
# You never edit this file. You just run it.
# -------------------------------------------------------

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectly_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
