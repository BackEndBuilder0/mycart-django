from django.urls import path

from .views import *

urlpatterns = [
    path('store/', store_page, name='store_page'),
    path('store/<slug:category_slug>', store_page, name='product_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>', product_details, name='product_by_productslug'),
    path('search', search, name='search'),

    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
]
