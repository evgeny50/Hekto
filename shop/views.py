from django.shortcuts import render, get_object_or_404

from . import services
from .models import Product
from cart.forms import CartAddProductForm


def home_page(request):
    featured_products = services.get_featured_products()
    last_product = services.get_last_products()
    return render(request, 'shop/home/home.html', {'featured_products': featured_products,
                                                   'last_product': last_product})


def detail_view(request, slug):
    product = get_object_or_404(Product.objects.select_related('category').defer(
        'code',
        'amount_of_views',
        'created',
        'updated'),
        slug=slug,
        available=True
    )
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail_view_product.html', {'product': product,
                                                             'cart_product_form': cart_product_form
                                                             })
