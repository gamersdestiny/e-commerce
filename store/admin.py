from django.contrib import admin

from .models import Category, Product, Ratings


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'category_created']


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'image', 'date_created']
    prepopulated_fields = {"slug": ("product_name",)}


@admin.register(Ratings)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'star']
    inlines = [ ProductInline ]