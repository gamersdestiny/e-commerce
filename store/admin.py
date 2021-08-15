from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from .models import Category, Product

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'category_created'] 

@admin.register(Product)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'image']