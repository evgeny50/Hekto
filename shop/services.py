from django.shortcuts import get_object_or_404

from .models import Category, Product


def get_featured_products():
    """
    Returns popular products
    sorted by amount of sales.
    """
    products = Product.objects.filter(available=True).only(
        'name', 'image', 'code', 'price', 'slug',
        'amount_of_sales', 'available').order_by('-amount_of_sales')[:4]
    return products


def get_last_products():
    """
    Returns last products
    sorted by date created.
    """
    last_products = Product.objects.filter(available=True).only(
        'name', 'slug', 'image', 'price',
        'sale_price', 'available', 'created'
    ).order_by('-created')[:6]
    return last_products


def get_products(slug):
    """
    Get all products and related data (Category) and delete
    unused fields (code, amount_of_views, created, updated).
    """
    products = get_object_or_404(Product.objects.select_related('category').defer(
        'code',
        'amount_of_views',
        'created',
        'updated'),
        slug=slug,
        available=True
    )
    return products


def get_categories():
    """Getting all categories and return their or 404 error"""
    categories = Category.objects.all()
    return categories


def get_products_by_category(slug):
    """Returns all products that belong to the category."""
    products = Product.objects.select_related('category').filter(category__slug=slug)
    return products
