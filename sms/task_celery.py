import jdatetime
from celery import shared_task
from sms.models import UploadFileModel


@shared_task
def send_sms_delay():
    for upload_file in UploadFileModel.objects.last():
        if jdatetime.datetime.hour == '8':
            upload_file.send_sms_birthday()
            upload_file.send_sms_contract()
            upload_file.send_sms_third_party_insurance()
            upload_file.send_sms_rental_insurance()
            upload_file.send_sms_technical_diagnoses()
