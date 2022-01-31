from django.shortcuts import render

from . import services


def home_page(request):
    featured_products = services.get_featured_products()
    last_product = services.get_last_products()
    return render(request, 'shop/home/home.html', {'featured_products': featured_products,
                                                   'last_product': last_product})


def detail_view(request, product):
    pass


