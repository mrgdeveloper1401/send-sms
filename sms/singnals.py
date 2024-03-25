from django.db.models.signals import post_save
from django.dispatch import receiver, Signal, dispatcher
from sms.models import SendMultiplesMessageModel
import requests


@receiver(post_save, sender=SendMultiplesMessageModel)
def send_sms_multiple_phone(sender, instance, created, **kwargs):
    if created:
        url = 'https://api.limosms.com/api/sendsms'
        receptor = [p.mobile_phone for p in instance.m2m_mobile_phone.all()]
        data = {
            'Message': instance.message_body,
            'SenderNumber': instance.from_user.mobile_phone,
            'MobileNumber': receptor
        }
        send_data = requests.post(url, json=data, headers={'ApiKey': 'c28b1f09-67b4-4728-a3c4-5352fee0b32d'})
        print(send_data.text)



