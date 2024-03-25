from django.contrib import admin
from sms.models import UploadFileModel, SendSingleMessageModel,  SendMultiplesMessageModel, PhoneBookModel


@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('execl_file', 'created_at', 'updated_at')
    list_display_links = ('created_at', 'updated_at')


@admin.register(SendSingleMessageModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'foreignkey_mobile_phone', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    list_per_page = 20
    date_hierarchy = 'created_at'
    list_editable = ('is_active',)


@admin.register(SendMultiplesMessageModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('m2m_mobile_phone',)


@admin.register(PhoneBookModel)
class PhoneBookModelAdmin(admin.ModelAdmin):
    pass
