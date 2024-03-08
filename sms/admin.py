from django.contrib import admin
from sms.models import UploadFileModel, SendSingleMessageModel,  SendMultiplesMessageModel, PhoneBookModel


@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('execl_file', 'created_at', 'updated_at')
    list_display_links = ('created_at', 'updated_at')


@admin.register(SendSingleMessageModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    pass


@admin.register(SendMultiplesMessageModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('m2m_mobile_phone',)


@admin.register(PhoneBookModel)
class PhoneBookModelAdmin(admin.ModelAdmin):
    pass
