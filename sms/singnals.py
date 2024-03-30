from django.db.models.signals import post_save
from django.dispatch import receiver, Signal, dispatcher
from sms.models import SendMultiplesMessageModel, SendSingleMessageModel, UploadFileModel
from kavenegar import *
import requests
import jdatetime


# api sms kavenegar
