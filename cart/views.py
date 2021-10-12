from django.shortcuts import render ,redirect,get_object_or_404
from Djangoecormeceapp .models import Products
from django.views.decorators.http import  require_POST
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request,products_id):
    cart = Cart(request)
    products = get_object_or_404(Products,id=products_id)
    form = CartAddProductForm(request.Post)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(products=products,quantity=cd ['quantity'],overide_quantity=cd['override'])
    return redirect_('cart_details')


def cart_remove(request,products_id):
    cart = Cart(request)
    products = get_object_or_404(Products,id=products_id)
    cart.remove(products)
    return redirect_('cart_details')


def cart_detail(request):
    cart = Cart(request)
    return render(request,"cart/cart.html",{'cart':cart})  
   
# Create your views here.
