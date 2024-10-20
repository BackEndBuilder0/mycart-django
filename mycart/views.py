from django.shortcuts import render
from pathlib import Path
from store.models import Product


def home_page(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    # print(Path(__file__).resolve().parent.parent) # output - /home/dev-lop/PycharmProjects/pythonProject/mycart
    return render(request, 'home.html', context)
