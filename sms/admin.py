from django.contrib import admin
from sms.models import UploadFileModel, SendSmsModel


@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('execl_file', 'created_at', 'updated_at')


@admin.register(SendSmsModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    pass
