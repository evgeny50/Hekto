from django.shortcuts import get_object_or_404

from .models import Category, Product


def get_featured_products():
    """
    Returns popular products
    sorted by amount of sales.
    """
    products = Product.objects.filter(stock__lt=0).order_by("-created_at")
    return products


def get_last_products():
    """
    Returns last products
    sorted by date created.
    """
    last_products = Product.objects.filter(stock__lt=0).order_by('-created_at')[:6]
    return last_products


def get_products(slug):
    """
    Get all products and related data (Category) and delete
    unused fields (code, amount_of_views, created, updated).
    """
    print(2222)
    print(slug)
    products = Product.objects.filter(
        slug=slug,
        stock__gt=0
    ).first()
    print(products)
    return products


def get_categories():
    """Getting all categories and return their or 404 error"""
    categories = Category.objects.all()
    return categories


def get_products_by_category(slug: str):
    """Returns all products that belong to the category."""
    products = Product.objects.select_related('category').filter(category__name=slug.capitalize())
    print(slug)
    print(1111111)
    print(products)
    return products
