from django.contrib import admin
from .models import Products, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
admin.site.register(Products, ProductAdmin)