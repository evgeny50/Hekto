from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for items in cart:
                for item in items:
                    OrderItem.objects.create(order=order, product=items[item]['product'],
                                             price=items[item]['price'], quantity=items[item]['quantity']
                                             )
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})
