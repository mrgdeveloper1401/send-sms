from enum import property
import jdatetime
from django.db import models
from core.models import UpdateModel, CreateModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import pandas as pd
from kavenegar import *
from send_sms.utils import SmsNegar, send_sms_user


class UploadFileModel(CreateModel, UpdateModel):
    execl_file = models.FileField(
        upload_to='execl_files/%y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'ods'])]
    )
    alt = models.TextField(_('توضیحی در مورد فایل'), blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.alt} -- {self.id}'

    @property
    def read_excel_file(self):
        f = self.execl_file
        read_excel_file = pd.read_excel(f)
        return read_excel_file

    def get_specified_info(self, column_name):
        info = self.read_excel_file.loc[0:][column_name]
        return info

    @property
    def show_specified_birthday(self):
        today = jdatetime.date.today()
        counter = 0
        birthday = self.get_specified_info('تاریخ تولد')
        birthday_list = []
        for b in birthday:
            counter += 1
            if today.month == b.month and today.day == b.day:
                show_user = self.read_excel_file.loc[counter - 1]
                birthday_list.append(show_user)
        return birthday_list

    def get_specified_user(self, column_name, days_to_check=5):
        today = jdatetime.date.today()
        five_days_ago = today + jdatetime.timedelta(days=days_to_check)
        counter = 0
        user_list = []
        info = self.get_specified_info(column_name)
        for item in info:
            counter += 1
            if (five_days_ago.year == item.year and five_days_ago.month == item.month and
                    five_days_ago.day == item.day):
                user = self.read_excel_file.loc[counter - 1]
                user_list.append(user)
        return user_list

    def send_sms_birthday(self):
        user_list = self.show_specified_birthday
        for user in user_list:
            full_name = user['نام و نام خوانوادگی']
            mobile = str(user['شماره همراه'])
            text = f' تولدتان مبارک باد{full_name}کاربر'
            send_message = SmsNegar(text, mobile)
            send_message.send_sms()
            print(send_message)

    def send_sms_contract(self):
        user_list = self.get_specified_user('قرارداد')
        send_sms_user(user_list, 'تا پایان قرار داد تان 5 روز باقی مانده هست')

    def send_sms_third_party_insurance(self):
        user_list = self.get_specified_user('بیمه شخص ثالث')
        send_sms_user(user_list, 'تا پایان بیمه شخص ثالث تان 5 روز باقی مانده هست')

    def send_sms_rental_insurance(self):
        user_list = self.get_specified_user('بیمه کرایه ای')
        send_sms_user(user_list, 'تا پایان بیمه کرایه تان 5 روز باقی مانده هست')

    def send_sms_technical_diagnoses(self):
        user_list = self.get_specified_user('معاینه فنی ')
        send_sms_user(user_list, 'تا پایان معاینه فنی تان 5 روز باقی مانده هست')
