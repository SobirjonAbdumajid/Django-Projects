from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, CodeConfirmation

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class CodeConfirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'code_token', 'created_at')

admin.site.register(CodeConfirmation, CodeConfirmationAdmin)
