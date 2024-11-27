from django.urls import path

from interface.views import payment
from interface.views.payment import payment_process, payment_done, payment_canceled

urlpatterns = [
    path('process/', payment_process, name='payment_process'),
    path('done/', payment_done, name='payment_done'),
    path('canceled/', payment_canceled, name='payment_canceled'),
]