from django.shortcuts import render
from ecommerceApp.models import Category, Product
import sqlite3 as sql

def index(request):
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT * FROM ecommerceApp_product')
    prods = cur.fetchall()
    dict = {'products': prods}
    return render(request, 'index.html', context= dict) 

def cart(request):
    return render(request, 'cart.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def order_complete(request):
    return render(request, 'order_complete.html')

def place_order(request):
    return render(request, 'place_order.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def register(request):
    return render(request, 'register.html')

def search_result(request):
    return render(request, 'search_result.html')

def signin(request):
    return render(request, 'signin.html')

def store(request,arg = None):
    if(arg == None):
        prods = Product.objects.all()
    else:
        temp = Category.objects.get(category_name = arg)
        prods = Product.objects.filter(category = temp)
    dict = {'products': prods,'count' : len(prods)}
    return render(request, 'store.html', context= dict)