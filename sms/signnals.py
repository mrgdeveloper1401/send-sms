from django.db.models.signals import post_save
from django.dispatch import receiver
from sms.models import SendSingleMessageModel
from send_sms.utils import send_single_sms_signals


@receiver(post_save, sender=SendSingleMessageModel)
def send_single_sms(sender, instance, created, **kwargs):
    if created:
        send_single_sms_signals(instance.foreignkey_mobile_phone.mobile_phone, instance.message_body,
                                instance.from_user.mobile_phone,)
