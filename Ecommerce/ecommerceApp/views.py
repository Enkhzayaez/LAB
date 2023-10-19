from django.shortcuts import render, redirect
from ecommerceApp.models import Category, Product
import sqlite3 as sql
from django.core.paginator import Paginator

def index(request):
    product = Product.objects.all()
    p = Paginator(product, 8)
    page = request.GET.get('page')
    page_products = p.get_page(page)
    dict = {'products': page_products}
    
    return render(request, 'index.html', context= dict) 

def cart(request):
    return render(request, 'cart.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def order_complete(request):
    return render(request, 'order_complete.html')

def place_order(request):
    return render(request, 'place_order.html')

def product_detail(request,c_slug, p_slug):
    product = Product.objects.get(category__c_slug = c_slug, p_slug = p_slug)
    return render(request, 'store/product_detail.html', {'single_product': product})

def register(request):
    return render(request, 'register.html')

def search_result(request):
    return render(request, 'search_result.html')

def signin(request):
    return render(request, 'signin.html')

def store(request,arg = None):
    if(arg == None):
        prods = Product.objects.all()
        p = Paginator(prods, 8)
        page = request.GET.get('page')
        page_products = p.get_page(page)
        count = prods.count()
    else:
        temp = Category.objects.get(category_name = arg)
        prods = Product.objects.filter(category = temp)

        p = Paginator(prods, 8)
        page = request.GET.get('page')
        page_products = p.get_page(page)
    dict = {'products': page_products,'count' : len(prods)}
    return render(request, 'store/store.html', context= dict)