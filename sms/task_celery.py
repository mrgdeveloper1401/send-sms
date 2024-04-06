from sms.models import UploadFileModel
from send_sms.celery import app


@app.task
def task_send_sms_birthday():
    send_sms = UploadFileModel.send_sms_birthday
    print(send_sms)


@app.task
def task_send_sms_contract():
    send_sms = UploadFileModel.send_sms_contract
    print(send_sms)


@app.task
def task_send_sms_third_party_insurance():
    send_sms = UploadFileModel.send_sms_third_party_insurance
    print(send_sms)


@app.task
def task_send_sms_rental_insurance():
    send_sms = UploadFileModel.send_sms_rental_insurance
    print(send_sms)


@app.task
def task_send_sms_technical_diagnoses():
    send_sms = UploadFileModel.send_sms_technical_diagnoses
    print(send_sms)
