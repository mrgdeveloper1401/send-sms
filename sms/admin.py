from django.contrib import admin
from sms.models import UploadFileModel


@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('execl_file', 'created_at', 'updated_at', 'id')
    list_display_links = ('created_at', 'updated_at')
