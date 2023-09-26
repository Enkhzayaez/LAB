from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def zurag(request):
    dic = {'print':'Энэ бол Django:'}
    return render(request, "appOne/zurag.html", context = dic)    

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

def store(request):
    return render(request, 'store.html')