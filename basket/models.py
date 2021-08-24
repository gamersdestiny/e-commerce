from django.db import models
from store.models import Product

class Basket(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField()
    def sub_total(self):
        qty = self.quantity
        price = self.product.price

        return price*qty

