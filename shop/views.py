from django.shortcuts import render, get_object_or_404

from . import services
from cart.forms import CartAddProductForm


def home_page(request):
    featured_products = services.get_featured_products()
    last_product = services.get_last_products()
    return render(request, 'shop/home/home.html', {'featured_products': featured_products,
                                                   'last_product': last_product})


def detail_view_product(request, slug):
    product = services.get_products(slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail_view_product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def categories_view(request):
    categories = services.get_categories()
    return render(request, 'shop/categories.html', {'categories': categories})


def detail_category(request, slug):
    products = services.get_products_by_category(slug)
    return render(request, 'shop/products_by_category.html', {'products': products})

