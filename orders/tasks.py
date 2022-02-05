from Hekto.celery import app

from django.core.mail import send_mail

from .models import Order


@app.task()
def order_created(order_id):
    """The task of sending email notifications
    on successful order placement."""
    order = Order.objects.get(id=order_id)
    subject = f'Order nr {order_id}'
    message = f'Dear {order.first_name},\n\nYou have successfully ' \
              f'placed an order. Your order id is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@hekto.com', [order.email])
    return mail_sent
