from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse
from ecommerceApp.models import Product

class Cart(models.Model):
    id = models.IntegerField()
    create_date = models.DateField(auto_now=True)
    def __str__ (self):
        return self.id
    
class CartItem(models.Model):
    c_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    def __str__ (self):
        return self.c_id
    