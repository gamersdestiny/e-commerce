from django import VERSION
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Name')
    category_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name