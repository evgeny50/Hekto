from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for items in cart:
                for item in items:
                    print(item)
                    OrderItem.objects.create(order=order, product=items[item]['product'],
                                             price=items[item]['price'], quantity=items[item]['quantity']
                                             )
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})
