#coding: utf8
from django.db.utils import IntegrityError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.

from linkparser.models import Goods

from .models import Cart, CartItem


def add_product_to_cart(request, product_id):
    if True:
        product = Goods.objects.get(pk=product_id)
        cart = request.user.cart
        try:
            create = Cart.objects.create(user=request.user)
            create_product = CartItem.objects.create(product=product)
            cart.cart.add(int(create_product.id))
            print create_product
            print cart
        except IntegrityError:
            create_product = CartItem.objects.create(product=product)
            cart.cart.add(int(create_product.id))
            messages.success(request, 'Вы добавили новый товар в корзину')
            return redirect('/')


def cart_list(request):
    user_cart = request.user.cart
    return render(request, 'cart/cart.html', {"cart": user_cart})




