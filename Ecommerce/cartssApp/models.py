from django.db import models
from ecommerceApp.models import Product

class Cartss(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartssItem(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    cart = models.ForeignKey(Cartss, models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product_name 

