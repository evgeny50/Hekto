from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='shop_home-page'),
    path('<slug:product>/', views.detail_view, name='product')
]