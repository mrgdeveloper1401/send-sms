# Generated by Django 5.0.2 on 2024-04-08 21:34

import django.core.validators
import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('mobile_phone', models.CharField(max_length=15, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Phone Book',
                'verbose_name_plural': 'Phone Books',
                'db_table': 'phone_book',
            },
        ),
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('execl_file', models.FileField(upload_to='execl_files/%y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'ods'])])),
                ('alt', models.TextField(blank=True, null=True, verbose_name='توضیحی در مورد فایل')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SendMultiplesMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('message_body', models.TextField(verbose_name='متن پیام')),
                ('from_user', models.ForeignKey(limit_choices_to={'is_superuser': True}, on_delete=django.db.models.deletion.PROTECT, related_name='sender_multiple_sms', to=settings.AUTH_USER_MODEL, verbose_name='از کاربر')),
                ('mobile_phones', models.ManyToManyField(related_name='m2m_mobile_phones', to='sms.phonebookmodel')),
            ],
            options={
                'verbose_name': 'send multiple sms',
                'verbose_name_plural': 'send multiple sms',
                'db_table': 'send_multiple_messages',
            },
        ),
        migrations.CreateModel(
            name='SendSingleMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('message_body', models.TextField(verbose_name='متن پیام')),
                ('from_user', models.ForeignKey(blank=True, default='', limit_choices_to={'is_superuser': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sender_single_sms', to=settings.AUTH_USER_MODEL, verbose_name='از کاربر')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='foreignkey_mobile_phone', to='sms.phonebookmodel', verbose_name='انتخاب شماره موبایل')),
            ],
            options={
                'verbose_name': 'send single sms',
                'verbose_name_plural': 'send single sms',
                'db_table': 'send_sms',
            },
        ),
    ]
