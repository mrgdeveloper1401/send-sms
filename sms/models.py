import os
from enum import property

import jdatetime
from django.db import models
from core.models import UpdateModel, CreateModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import pandas as pd
from kavenegar import *


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

    @property
    def get_full_name(self):
        full_name = self.read_excel_file.loc[0:]['نام و نام خوانوادگی']
        return full_name

    @property
    def get_mobile_phone(self):
        mobile_phone = self.read_excel_file.loc[0:]['شماره همراه']
        return mobile_phone

    @property
    def get_birthday(self):
        birthday = self.read_excel_file.loc[0:]['تاریخ تولد']
        return birthday

    @property
    def get_contract(self):
        contract = self.read_excel_file.loc[0:]['قرارداد']
        return contract

    @property
    def get_third_party_insurance(self):
        third_party_insurance = self.read_excel_file.loc[0:]['بیمه شخص ثالث']
        return third_party_insurance

    @property
    def get_rental_insurance(self):
        rental_insurance = self.read_excel_file.loc[0:]['بیمه کرایه ای']
        return rental_insurance

    @property
    def get_technical_diagnoses(self):
        technical_diagnoses = self.read_excel_file.loc[0:]['معاینه فنی']
        return technical_diagnoses

    @property
    def show_specified_birthday(self):
        today = jdatetime.date.today()
        counter = 0
        birthday = self.get_birthday
        birthday_list = []
        for b in birthday:
            counter += 1
            if today.month == b.month and today.day == b.day:
                show_user = self.read_excel_file.loc[counter - 1]
                birthday_list.append(show_user)
        return birthday_list

    @property
    def show_specified_contract(self):
        today = jdatetime.date.today()
        five_days_later = today + jdatetime.timedelta(days=5)
        counter = 0
        contract = self.get_contract
        contract_list = []
        for c in contract:
            counter += 1
            if five_days_later.year == c.year and five_days_later.month == c.month and five_days_later.day == c.day:
                show_user = self.read_excel_file.loc[counter - 1]
                contract_list.append(show_user)
        return contract_list

    @property
    def five_days_later(self):
        today = jdatetime.date.today()
        five_days_later = today + jdatetime.timedelta(days=5)
        return five_days_later

    @property
    def show_specified_third_party_insurance(self):
        counter = 0
        third_party_insurance_list = []
        third_party_insurance = self.get_third_party_insurance
        for t in third_party_insurance:
            counter += 1
            if (self.five_days_later.year == t.year and self.five_days_later.month == t.month and
                    self.five_days_later.day == t.day):
                show_user = self.read_excel_file.loc[counter - 1]
                third_party_insurance_list.append(show_user)
        return third_party_insurance_list

    @property
    def show_rental_insurance(self):
        counter = 0
        rental_insurance_list = []
        rental_insurance = self.get_rental_insurance
        for r in rental_insurance:
            counter += 1
            if (self.five_days_later.year == r.year and self.five_days_later.month == r.month
                    and self.five_days_later.day == r.day):
                show_user = self.read_excel_file.loc[counter - 1]
                rental_insurance_list.append(show_user)
        return rental_insurance_list

    @property
    def show_technical_diagnoses(self):
        counter = 0
        technical_diagnose_list = []
        technical_diagnose = self.get_technical_diagnoses
        for t in technical_diagnose:
            counter += 1
            if (self.five_days_later.year == t.year and self.five_days_later.month == t.month
                    and self.five_days_later.day == t.day):
                show_user = self.read_excel_file.loc[counter - 1]
                technical_diagnose_list.append(show_user)
        return technical_diagnose_list

    def send_sms(self, mobiles, message):
        try:
            api_key = os.environ.get('API_KEY')
            api = KavenegarAPI(api_key)
            params = {
                'sender': '',
                'receptor': mobiles,
                'message': message,
            }
            response = api.sms_sendarray(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)

    def send_sms_birthday(self):
        trustees_today = self.show_specified_birthday
        combined_list = []
        for trustee in trustees_today:
            full_name = trustee['نام و نام خوانوادگی']
            mobile = trustee['شماره همراه']
            combined_list.append((full_name, mobile))
        while len(combined_list) > 0:
            full_name, mobile = combined_list.pop(0)
            text = f'کاربر {full_name} تولدتات مبارک باد'
            self.send_sms(mobile, full_name)

    def send_sms_contract(self):
        combined_list = []
        for contract in self.show_specified_contract:
            full_name = contract['نام و نام خوانوادگی']
            mobiles = contract['شماره همراه']
            combined_list.append((full_name, mobiles))
        while len(combined_list) > 0:
            full_name, mobile = combined_list.pop(0)
            self.send_sms(mobile, full_name)

    def send_sms_third_party_insurance(self):
        combined_list = []
        for tpi in self.show_specified_third_party_insurance:
            full_name = tpi['نام و نام خوانوادگی']
            mobiles = tpi['شماره همراه']
            combined_list.append((full_name, mobiles))
        while len(combined_list) > 0:
            full_name, mobile = combined_list.pop(0)
            self.send_sms(mobile, full_name)

    def send_sms_rental_insurance(self):
        combined_list = []
        for ri in self.show_rental_insurance:
            full_name = ri['نام و نام خوانوادگی']
            mobiles = ri['شماره همراه']
            combined_list.append((full_name, mobiles))
        while len(combined_list) > 0:
            full_name, mobile = combined_list.pop(0)
            self.send_sms(mobile, full_name)

    def send_sms_technical_diagnoses(self):
        combined_list = []
        for td in self.show_technical_diagnoses:
            full_name = td['نام و نام خوانوادگی']
            mobile = td['شماره همراه']
            combined_list.append((full_name, mobile))
        while len(combined_list) > 0:
            full_name, mobile = combined_list.pop(0)
            self.send_sms(mobile, full_name)


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
                                  default=None)
    foreignkey_mobile_phone = models.ForeignKey(PhoneBookModel, on_delete=models.PROTECT,
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
