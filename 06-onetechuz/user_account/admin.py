from django.contrib import admin
from .models import CustomUser, CodeConfirmation


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_at']


@admin.register(CodeConfirmation)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'code', 'code_token']
