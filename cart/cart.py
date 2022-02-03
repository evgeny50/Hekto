from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart object. If no cart
        object, save an empty cart in the session.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Go through the items in the shopping
        cart and get the Product objects.
        """
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        yield item

    def __len__(self):
        """Return total quantity products in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity, update_quantity=False):
        """Add product to the cart or update it's quantity."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[str(product_id)] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def clear(self):
        """Creat cart."""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        """Remove product from cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
