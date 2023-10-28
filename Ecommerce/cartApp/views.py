from django.shortcuts import render

# Create your views here.
def index(request):
    session_key =  _cart_id(request)
    return render(request,'cart.html')

def _cart_id(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    
    return request.session.session_key

def _cart_id(request):
    return render(request, 'cart.html')
