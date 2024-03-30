import datetime

import jdatetime
import pandas
from django.db import models
from core.models import UpdateModel, CreateModel
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django_jalali.db import models as django_jalali_models
import pandas as pd
import openpyxl as opx
import requests


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
        full_name = self.read_excel_file.loc[0:]['full_name']
        return full_name

    @property
    def get_mobile_phone(self):
        mobile_phone = self.read_excel_file.loc[0:]['mobile_phone']
        return mobile_phone

    @property
    def get_birthday(self):
        birthday = self.read_excel_file.loc[0:]['birthday']
        return birthday

    @property
    def get_contract(self):
        contract = self.read_excel_file.loc[0:]['contract']
        return contract

    @property
    def get_third_party_insurance(self):
        third_party_insurance = self.read_excel_file.loc[0:]['third_party_insurance']
        return third_party_insurance

    @property
    def get_rental_insurance(self):
        rental_insurance = self.read_excel_file.loc[0:]['rental_insurance']
        return rental_insurance

    @property
    def get_technical_diagnoses(self):
        technical_diagnoses = self.read_excel_file.loc[0:]['technical_diagnoses']
        return technical_diagnoses


    def specified_birhday(self):
        today = datetime.date(year=2000, month=1, day=1)
        counter = 0
        birthday = self.get_birthday
        for b in birthday:
            if today.month == b.month and today.day == b.day:
                counter += 1
                show_user = self.read_excel_file.loc[counter - 1]
                return show_user
            else:
                counter = 0




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
                                  related_name='sender_single_sms', limit_choices_to={'is_superuser': True})
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
