from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cart_page, name='cart_page'),
    path('cart/<int:product_id>/', add_cart, name='add_to_card_page'),
    path('cart_remove/<int:product_id>/', remove_cart, name='remove_to_card_page'),
]