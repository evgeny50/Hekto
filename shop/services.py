from .models import Product


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
