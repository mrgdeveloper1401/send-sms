from django.contrib import admin
from accounts.models import User, UserDeleted, OtpCode
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "username")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "password1", "password2"),
            },
        ),
    )
    list_display = ('mobile_phone', "username", "email", "first_name", "last_name", "is_staff", 'is_superuser',
                    'is_active',
                    'is_deleted')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups",
                   ('date_joined', JDateFieldListFilter))
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_display_links = ('mobile_phone', 'username', 'email')
    readonly_fields = ('date_joined', 'last_login')
    date_hierarchy = 'date_joined'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)


@admin.register(UserDeleted)
class UserDeletedAdmin(admin.ModelAdmin):
    list_display = ('mobile_phone', "username", "email", "first_name", "last_name", "is_staff", 'is_active',
                    'is_deleted', 'deleted_at')
    actions = ('recovery_user', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=True)

    @admin.action(description='recovery user')
    def recovery_user(modeladmin, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    pass
