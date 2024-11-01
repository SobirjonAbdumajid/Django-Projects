from django.contrib import admin
from .models import MaqolaModel

# Register your models here.
@admin.register(MaqolaModel)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags')
    class Meta:
        model = MaqolaModel
