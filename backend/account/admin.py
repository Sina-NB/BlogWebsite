from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff', 'is_superuser', 'is_active', 'last_login']
    list_filter = ['email', 'is_staff', 'is_superuser', 'is_active']
    searching_fields = ['email']
    ordering = ['email']
    fieldsets = [
        ['Authentication', {'fields': ['email', 'password']}],
        ['Permissions', {'fields': ['groups', 'user_permissions', 'is_staff', 'is_superuser', 'is_active']}],
    ]
    add_fieldsets = [
        ['Authentication', {'fields': ['email', 'password1', 'password2']}],
        ['Permissions', {'fields': ['is_staff', 'is_superuser', 'is_active']}]
    ]
