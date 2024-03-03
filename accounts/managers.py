from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, mobile_phone, password=None, **extra_fields):
        if not mobile_phone:
            raise ValueError('mobile phone must be provided')
        user = self.model(mobile_phone=mobile_phone, **extra_fields)
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_phone, password=None, **extra_fields):
        user = self.create_user(mobile_phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
