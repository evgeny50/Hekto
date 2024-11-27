from django.shortcuts import render, redirect

from core.orders.forms import OrderCreateForm
from core.cart.cart import Cart
from core.shop.models import OrderItem


def order_create(request):
    if not request.user.is_authenticated:

        return redirect('customer_login')
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
            # order_created.delay(order.id)
            # request.session['order_id'] = order.id
            # return redirect(reverse('payment_process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})
