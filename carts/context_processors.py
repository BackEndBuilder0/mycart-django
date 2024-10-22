from .models import Cart, CartItem
from .views import _cart_id


def cart_counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            carte_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in carte_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
