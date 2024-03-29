import pandas
from django.db import models
from core.models import UpdateModel, CreateModel
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django_jalali.db import models as django_jalali_models
import pandas as pd
import requests


class UploadFileModel(CreateModel, UpdateModel):
    execl_file = models.FileField(
        upload_to='execl_files/%y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )
    alt = models.TextField(_('توضیحی در مورد فایل'), blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.alt} -- {self.id}'

    @property
    def mobile_phone(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        mobile_phone = pandas_excel_file['mobile_phone']
        return mobile_phone

    @property
    def birth_day(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        birth_day = pandas_excel_file['birthday']
        return birth_day

    @property
    def contract(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        contract = pandas_excel_file['contract']
        return contract

    @property
    def third_party_insurance(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        third_party_insurance = pandas_excel_file['Third_party_insurance']
        return third_party_insurance

    @property
    def rental_insurance(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        rental_insurance = pandas_excel_file['rental_insurance']
        return rental_insurance

    @property
    def technical_diagnosis(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        technical_diagnosis = pandas_excel_file['technical_diagnosis']
        return technical_diagnosis


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
