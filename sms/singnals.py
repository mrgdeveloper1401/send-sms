from django.db.models.signals import post_save
from django.dispatch import receiver, Signal, dispatcher
from sms.models import SendMultiplesMessageModel, SendSingleMessageModel
from kavenegar import *
import requests


# api sms negar
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
            'cUserName': 'tarabar.sina',
            'cPassword': 'Aa123456',
            'cDomainname': 'sms.smsnegar.com',
            'Getid': [],
            'nTypeSent': 2,
            'nSpeedsms': 0,
            'nPeriodmin': 0,
            'cstarttime': [],
            'cEndTime': []
        }
        send_sms = requests.post(url, json=data)
        print(send_sms)


@receiver(post_save, sender=SendSingleMessageModel)
def send_single_sms_kavenegar(sender, instance, created, **kwargs):
    if created:
        try:
            import json
        except ImportError:
            import simplejson as json
        try:
            api_key = '4755754B6A505230624D575A396531366B6E4269397952356C6345786843766477444338586F454C354E6B3D'
            api = KavenegarAPI({'api_key': api_key})
            params = {
                'sender': instance.from_user.mobile_phone,
                'receptor': instance.foreignkey_mobile_phone.mobile_phone,
                'message': instance.message_body,
            }
            response = api.sms_send(params)
            print(str(response))
        except APIException as e:
            print(str(e))
        except HTTPException as e:
            print(str(e))


@receiver(post_save, sender=SendMultiplesMessageModel)
def send_single_sms_kavenegar(sender, instance, created, **kwargs):
    if created:
        try:
            import json
        except ImportError:
            import simplejson as json
        try:
            api_key = '4755754B6A505230624D575A396531366B6E4269397952356C6345786843766477444338586F454C354E6B3D'
            api = KavenegarAPI({'api_key': api_key})
            params = {
                'sender': instance.from_user.mobile_phone,
                'receptor': instance.all_number,
                'message': instance.message_body,
            }
            response = api.sms_send(params)
            print(str(response))
        except APIException as e:
            print(str(e))
        except HTTPException as e:
            print(str(e))



