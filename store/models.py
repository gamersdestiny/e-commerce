from store.views import product
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Name')
    category_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return f'Ratings {str(self.star)}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ratings = models.ForeignKey(Ratings, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name='Name')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name


