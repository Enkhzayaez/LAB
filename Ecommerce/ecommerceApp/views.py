from django.shortcuts import render, redirect
from ecommerceApp.models import Category, Product
import sqlite3 as sql
from django.core.paginator import Paginator

def index(request):
    if request.GET.get("search"):
        search_query = request.GET.get("search")
        product = Product.objects.filter(product_name__icontains=search_query)
    else:
        product = Product.objects.all()
    p = Paginator(product, 8)
    page = request.GET.get('page')
    page_products = p.get_page(page)
    dict = {'products': page_products}
        
    return render(request, 'index.html', context= dict) 

# def cart(request):
#     return render(request, 'cart.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def order_complete(request):
    return render(request, 'order_complete.html')

def place_order(request):
    return render(request, 'place_order.html')

def product_detail(request,c_slug, p_slug):
    product = Product.objects.get(category__c_slug = c_slug, p_slug = p_slug)
    return render(request, 'store/product_detail.html', {'single_product': product})

def search_result(request):
    return render(request, 'search_result.html')

def store(request, arg=None):

    if arg is None:
        prods = Product.objects.all()

        # Filter based on search query
        search_query = request.GET.get("search")
        search_min_price = request.GET.get("minprice")
        search_max_price = request.GET.get("maxprice")
        if search_query:
            prods = prods.filter(product_name__icontains=search_query)
        elif search_min_price:
            prods = prods.filter(price__gte=search_min_price, price__lte=search_max_price)

    else:
        temp = Category.objects.get(category_name=arg)
        prods = Product.objects.filter(category=temp)

        # Filter based on search query within a category
        search_query = request.GET.get("search")
        search_min_price = request.GET.get("minprice")
        search_max_price = request.GET.get("maxprice")
        if search_query:
            prods = prods.filter(product_name__icontains=search_query)
        elif search_min_price:
                    prods = prods.filter(price__gte=search_min_price, price__lte=search_max_price)
    p = Paginator(prods, 8)
    page = request.GET.get('page')
    page_products = p.get_page(page)
    count = len(prods)

    context = {'products': page_products, 'count': count}
    return render(request, 'store/store.html', context=context)