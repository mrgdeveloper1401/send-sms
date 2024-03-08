import pandas
from django.db import models
from core.models import UpdateModel, CreateModel
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django_jalali.db import models as django_jalali_models
import pandas as pd


class UploadFileModel(CreateModel, UpdateModel):
    execl_file = models.FileField(
        upload_to='execl_files/%y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )

    @property
    def mobile_phone(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        mobile_phone = pandas_excel_file['mobile phone']
        return mobile_phone

    @property
    def birth_day(self):
        read_excel_file = self.execl_file
        pandas_excel_file = pd.read_excel(read_excel_file)
        birth_day = pandas_excel_file['birthday']
        return birth_day


class SendSmsModel(CreateModel):
    execl_file = models.FileField(upload_to='execl_files/%y/%m/%d')
    from_user = models.ForeignKey(verbose_name='از کاربر', to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                  related_name='sender', limit_choices_to={'is_superuser': True})
    to_mobile_phone = models.ForeignKey(verbose_name=_("به شماره همراه"), to=UploadFileModel,
                                        related_name='upload_file',
                                        blank=True, null=True, on_delete=models.PROTECT)
    message_body = models.TextField(_('متن پیام'))
    send_time = django_jalali_models.jDateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'send_sms'
        verbose_name = _('send sms')
        verbose_name_plural = _("send_sms")

