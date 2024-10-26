from django.shortcuts import render, get_object_or_404
from .models import *
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# Create your views here.
def store_page(request, category_slug=None, product_slug=None):
    categories = None
    products = None
    # product = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
    # elif product_slug != None:
    #     product = get_object_or_404(Product, slug=product_slug)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)

    context = {
        'products': paged_product,
        # 'product': product,
    }
    return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'prod': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product-detail.html', context)


def search(request):
    products = None
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            products = Product.objects.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            ).order_by('-created_date')
    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)