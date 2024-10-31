from django.shortcuts import render
from pathlib import Path
from store.models import Product, ReviewRating


def home_page(request):
    products = Product.objects.all().filter(is_available=True)
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
