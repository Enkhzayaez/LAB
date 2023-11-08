from django.shortcuts import render , redirect

from ecommerceApp.models import Product
from .models import Cartss, CartssItem 


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id 

def index(request,total = 0, quantity = 0, cart_items = None):
    try: 
        cart = Cartss.objects.get(cart_id = _cart_id)
    except Cartss.DoesNotExist:
        cart = Cartss.objects.create(cart_id = _cart_id)
    cart.save()

    cart_items = CartssItem.objects.filter(cart=cart, is_active = True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }

    return render(request,'cart.html',context)



def add_cart(request, product_id ):
    product=Product.objects.get(id=product_id)
    try: 
        cart=Cartss.objects.get(cart_id=_cart_id(request))
    except Cartss.DoesNotExist:
        cart=Cartss.objects.create(cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item=CartssItem.objects.get(cart=cart, product=product)
        if cart_item.quantity <cart_item.product.stock:
            cart_item.quantity +1
        cart.save()
    except CartssItem.DoesNotExist:
        cart_item=CartssItem.objects.create(product=product, cart=cart, quantity=1)
    cart.save()
    return redirect('cart',)
def remove_cart(request, product_id):
    cart = Cartss.objects.get(cart_id=_cart_id(request))
    product = Product.objects.get(Product, id = product_id)
    cart_item = CartssItem.objects.get(product=product, cart=cart)
    if cart_item.quantity >1 :
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart")

def remove_cartItem(request, product_id):
    cart = Cartss.objects.get(cart_id= _cart_id(request))
    product = Product.objects.get(Product, id = product_id)
    cart_item = CartssItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect("cart")