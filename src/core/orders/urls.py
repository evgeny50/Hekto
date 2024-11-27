from django.urls import path

from interface.views import order
from interface.views.order import order_create

urlpatterns = [
    path('create/', order_create, name='order_create'),
]