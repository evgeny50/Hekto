from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import ProductForm
from . import services
from cart.forms import CartAddProductForm
from .models import Product


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


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product', slug=product.slug)
    else:
        form = ProductForm()
    return render(request, 'shop/create_product.html', {'form': form})


def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', slug=product.slug)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})



def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'shop/delete_product.html', {'product': product})


