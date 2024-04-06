from celery import Celery
import os

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_sms.settings')

app = Celery('send_sms')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'task_send_sms_birthday': {
        'task': 'sms.task_celery.task_send_sms_birthday',
        'schedule': crontab(hour='8', minute='0'),
    },
    'task_send_sms_contact': {
        'task': 'sms.task_celery.task_send_sms_contract',
        'schedule': crontab(hour='8', minute='0')
    },
    'task_send_sms_third_rental_insurance': {
        'task': 'sms.task_celery.task_send_sms_third_party_insurance',
        'schedule': crontab(hour='8', minute='0')
    },
    'task_send_sms_rental_insurance': {
        'task': 'sms.task_celery.task_send_sms_rental_insurance',
        'schedule': crontab(hour='8', minute='0')
    },
    'task_send_sms_technical_diagnoses': {
        'task': 'sms.task_celery.task_send_sms_technical_diagnoses',
        'schedule': crontab(hour='8', minute='0')
    },

}
