# apps.py
# -------------------------------------------------------
# WHAT IS THIS FILE?
# This registers your app with Django.
# Django needs to know your app exists before it can use it.
# Think of it like signing in at reception before a meeting.
# -------------------------------------------------------

from django.apps import AppConfig


class ConnectlyApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connectly_api'
