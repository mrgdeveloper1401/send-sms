from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django_jalali.db import models as jmodels
from accounts.managers import UserManager
from core.models import SoftDeleteModel, CreateModel, UpdateModel


class User(AbstractUser, SoftDeleteModel):
    mobile_phone = models.CharField(max_length=15, unique=True)
    date_joined = jmodels.jDateTimeField(blank=True, null=True, default=now())
    last_login = jmodels.jDateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_phone'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.mobile_phone

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserDeleted(User):
    class Meta:
        proxy = True


class OtpCode(CreateModel):
    code = models.PositiveSmallIntegerField()
    time_validity = models.TimeField()

    class Meta:
        db_table = 'otp_code'
        verbose_name = _('otp code')
        verbose_name_plural = _('otp codes')
