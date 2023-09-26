from django.shortcuts import render, redirect
from ecommerceApp.models import Item, Category
from ecommerceApp.forms import ItemForm
from ecommerceApp import forms

def index(request):
    item_list = Item.objects.all()
    item_dictionary = {'items': item_list}
    return render(request, 'index.html', context=item_dictionary)

def itemAdd(request):
    itemForm = forms.ItemForm()
    
    if request.method == 'POST':
        itemForm_req = forms.ItemForm(request.POST)
        if itemForm_req.is_valid():
            mv = Item.objects.get_or_create(
            name=itemForm_req.cleaned_data['name'],
            price=itemForm_req.cleaned_data['price'],
            category=itemForm_req.cleaned_data['category'])[0]
            mv.save()
            return redirect('index')
        return render(request, 'itemAdd.html',{'itemForm':itemForm})
