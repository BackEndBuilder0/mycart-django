from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import CartItem, Cart
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) # Get the product for Cart
    color = request.GET.get('color')
    size = request.GET.get('size')
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print(f'This is Try Block Cart : {cart}')
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
        print(f'This is Except Block Cart : {cart}')
    print(f'This is outside Try Except Block Cart : {cart}')

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
        print(f'This is Try Block of CartItem : {cart_item}')
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,
            color = color,
            size = size,

        )
        cart_item.save()
        print(f'This is Except Block of CartItem : {cart_item}')
    print(f'This is outside Try Except Block of CartItem : {cart_item}')
    return redirect('cart_page')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)  # Get the product for Cart
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_page')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)  # Get the product for Cart
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_page')


def cart_page(request, total_price=0, quantity=0, cart_items=None):
    tax=0
    grand_total=0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total_price += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (18 * total_price) / 100
        grand_total = total_price+tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total_price,
        'quantity' : quantity,
        'cart_items': cart_items,
        'tax': round(tax),
        'grand_total': round(grand_total),
    }

    return render(request, 'store/cart.html', context)