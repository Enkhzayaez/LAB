from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    c_slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    def __str__ (self):
        return self.category_name
    def get_url(self):
        return reverse('store', args=[self.c_slug])
    
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    p_slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True) 
    def __str__ (self):
        return self.product_name
    def get_url(self):
        return reverse('product_detail', args=[self.category.c_slug, self.p_slug])