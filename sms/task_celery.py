from celery import shared_task
from send_sms.utils import SmsNegar
from sms.models import UploadFileModel


@shared_task
def task_send_sms_birthday():
    upload_file = UploadFileModel.objects.last()
    if upload_file:
        sms_message = upload_file.send_sms_birthday
        return sms_message


@shared_task
def task_send_sms_contract():
    upload_file = UploadFileModel.objects.last()
    if upload_file:
        sms_message = upload_file.send_sms_contract
        return sms_message


@shared_task
def task_send_sms_third_party_insurance():
    upload_file = UploadFileModel.objects.last()
    if upload_file:
        sms_message = upload_file.send_sms_third_party_insurance
        return sms_message


@shared_task
def task_send_sms_rental_insurance():
    upload_file = UploadFileModel.objects.last()
    if upload_file:
        sms_message = upload_file.send_sms_rental_insurance
        return sms_message


@shared_task
def task_send_sms_technical_diagnoses():
    upload_file = UploadFileModel.objects.last()
    if upload_file:
        sms_message = upload_file.send_sms_technical_diagnoses
        return sms_message
