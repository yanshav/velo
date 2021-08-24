from django.shortcuts import render, get_object_or_404, redirect
from velo.models import Marsh
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.signals import user_logged_in




# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    user_id=request.user.id
    print(user_id)
    if not cart:
        cart = request.session.create()
    return (cart,user_id)


def add_cart(request, marsh_id):
    marsh_name = Marsh.objects.get(id=marsh_id)
    cart_id, user_id = _cart_id(request)
    try:
        cart = Cart.objects.get(user_id=user_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id,user_id=user_id)
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=marsh_name, cart=cart)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=marsh_name, cart=cart)
        cart_item.save()
    return redirect('saved')


from django.contrib.auth.decorators import login_required


@login_required
def cart_detail(request, cart_items=None):
    cart_id, user_id = _cart_id(request)
    try:
        cart = Cart.objects.get(user_id=user_id)
        cart_items = CartItem.objects.filter(cart=cart)

    except ObjectDoesNotExist:
        pass

    return render(request, 'save/saved.html', dict(cart_items=cart_items))
