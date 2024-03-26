from django.db.models.signals import post_save
from django.dispatch import receiver, Signal, dispatcher
from sms.models import SendMultiplesMessageModel, SendSingleMessageModel
import requests


@receiver(post_save, sender=SendSingleMessageModel)
def send_single_sms(sender, instance, created, **kwargs):
    if created:
        url = 'https://sms.smsnegar.com/SendSms'
        data = {
            'smsbody': instance.message_body,
            'smsNumber': [instance.foreignkey_mobile_phone.mobile_phone],
            'SenderNumber': instance.from_user.mobile_phone,
            'nCmessage': '1',
            'm-scheuleDate': 'Null',
            'cFormNumber': 'Null',
            'username': 'tarabar.sina',
            'password': 'Aa123456',
            'cDomainName': 'sms.smsnegar.com'
        }
        send_sms = requests.post(url, json=data)
        print(send_sms)

