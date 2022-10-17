from asyncore import read
import imp
from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'

    # def ready(self):
    #     super().ready()
    #     from appointment import signals


