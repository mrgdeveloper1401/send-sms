from django.db.models.signals import post_save
from django.dispatch import receiver, Signal, dispatcher
from sms.models import SendSingleMessageModel
import requests


@receiver(post_save, sender=SendSingleMessageModel)
def send_sms(sender, instance, created, **kwargs):
    if created:
        url = 'https://api.limosms.com/api/sendsms'
        rec = str(instance.to_mobile_phone)
        receptor = [rec]
        myobj = {
            'Message': instance.message_body,
            'MobileNumber': receptor,
            'SenderNumber': instance.from_user
        }
        x = requests.post(url, myobj, headers={'ApiKey': 'c28b1f09-67b4-4728-a3c4-5352fee0b32d'})
        print(x.text)
