from django.contrib import admin
from .models import Maqola

class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'tag', 'rank', 'age', 'address')

admin.site.register(Maqola, MaqolaAdmin)
