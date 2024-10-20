from shutil import ExecError
from unicodedata import category

from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def store_page(request, category_slug=None, product_slug=None):
    categories = None
    products = None
    product = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    elif product_slug != None:
        product = get_object_or_404(Product, slug=product_slug)
    else:
        products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
        'product': product,
    }
    return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'prod': single_product,
    }
    return render(request, 'store/product-detail.html', context)