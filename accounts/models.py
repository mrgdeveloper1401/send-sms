from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager
from core.models import SoftDeleteModel


class User(AbstractUser, SoftDeleteModel):
    mobile_phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_phone'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserDeleted(User):
    class Meta:
        proxy = True
