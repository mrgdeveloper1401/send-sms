from django.contrib import admin
from sms.models import UploadFileModel, SendSingleMessageModel,  SendMultiplesMessageModel, PhoneBookModel


@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('execl_file', 'created_at', 'updated_at', 'id')
    list_display_links = ('created_at', 'updated_at')


@admin.register(SendSingleMessageModel)
class SendSmsModelAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'foreignkey_mobile_phone', 'created_at')
    list_filter = ('created_at', )
    list_per_page = 20
    date_hierarchy = 'created_at'


@admin.register(SendMultiplesMessageModel)
class SendMultipleSmsAdmin(admin.ModelAdmin):
    filter_horizontal = ('mobile_phones', )
    # list_display = ('all_number', )


@admin.register(PhoneBookModel)
class PhoneBookModelAdmin(admin.ModelAdmin):
    pass
