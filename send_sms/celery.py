from celery import Celery
import os

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_sms.settings')

app = Celery('send_sms')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
