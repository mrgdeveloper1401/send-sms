from enum import property
import jdatetime
from django.db import models
from core.models import UpdateModel, CreateModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import pandas as pd
from kavenegar import *
from send_sms.utils import SmsNegar


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

    def send_sms_user(self, user_list, message):
        for user in user_list:
            full_name = user['نام و نام خوانوادگی']
            mobile = str(user['شماره همراه'])
            text = f'کاربر {full_name} {message}'
            send_message = SmsNegar(mobile, text)
            send_message.send_sms()
            print(send_message)

    def send_sms_birthday(self):
        user_list = self.show_specified_birthday
        for user in user_list:
            full_name = user['نام و نام خوانوادگی']
            mobile = user['شماره همراه']
            text = f' تولدتان مبارک باد{full_name}کاربر'
            send_message = SmsNegar(text, mobile)
            send_message.send_sms()
            print(send_message)

    def send_sms_contract(self):
        user_list = self.get_specified_user('قرارداد')
        self.send_sms_user(user_list, 'تا پایان قرار داد تان 5 روز باقی مانده هست')

    def send_sms_third_party_insurance(self):
        user_list = self.get_specified_user('بیمه شخص ثالث')
        self.send_sms_user(user_list, 'تا پایان بیمه شخص ثالث تان 5 روز باقی مانده هست')

    def send_sms_rental_insurance(self):
        user_list = self.get_specified_user('بیمه کرایه ای')
        self.send_sms_user(user_list, 'تا پایان بیمه کرایه تان 5 روز باقی مانده هست')

    def send_sms_technical_diagnoses(self):
        user_list = self.get_specified_user('معاینه فنی ')
        self.send_sms_user(user_list, 'تا پایان معاینه فنی تان 5 روز باقی مانده هست')


class PhoneBookModel(CreateModel, UpdateModel):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    mobile_phone = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.mobile_phone

    class Meta:
        db_table = 'phone_book'
        verbose_name = _("Phone Book")
        verbose_name_plural = _("Phone Books")


class SendSingleMessageModel(CreateModel):
    from_user = models.ForeignKey(verbose_name='از کاربر', to='accounts.User', on_delete=models.PROTECT,
                                  related_name='sender_single_sms', limit_choices_to={'is_superuser': True},
                                  blank=True, null=True,
                                  default='')
    to_user = models.ForeignKey(PhoneBookModel, on_delete=models.PROTECT,
                                related_name='foreignkey_mobile_phone',
                                verbose_name=_('انتخاب شماره موبایل'))
    message_body = models.TextField(_('متن پیام'))

    class Meta:
        db_table = 'send_sms'
        verbose_name = _('send single sms')
        verbose_name_plural = _("send single sms")


class SendMultiplesMessageModel(CreateModel, UpdateModel):
    from_user = models.ForeignKey(verbose_name='از کاربر', to='accounts.User', on_delete=models.PROTECT,
                                  related_name='sender_multiple_sms', limit_choices_to={'is_superuser': True})
    mobile_phones = models.ManyToManyField(PhoneBookModel, related_name='m2m_mobile_phones')
    message_body = models.TextField(_('متن پیام'))

    @property
    def all_number(self):
        mobile_phones = [p.mobile_phone for p in self.mobile_phones.all()]
        return mobile_phones

    class Meta:
        db_table = 'send_multiple_messages'
        verbose_name = _('send multiple sms')
        verbose_name_plural = _("send multiple sms")
