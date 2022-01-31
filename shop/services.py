from .models import Product


def get_featured_products():
    """
    Returns popular products
    sorted by amount of sales.
    """
    products = Product.objects.filter(available=True).order_by('-amount_of_sales')[:4]
    return products


def get_last_products():
    """
    Returns last products
    sorted by date created.
    """
    last_products = Product.objects.filter(available=True).order_by('-created')[:6]
    return last_products
