from django.contrib import admin
from ecommerceApp.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'c_slug': ('category_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'p_slug': ('product_name',)}
admin.site.register(Product, ProductAdmin)
