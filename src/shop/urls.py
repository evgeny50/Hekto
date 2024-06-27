from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.categories_view, name='categories'),
    path('category/<slug:slug>/', views.detail_category, name='category'),
    path('', views.home_page, name='shop_home-page'),
    path('<slug:slug>/', views.detail_view_product, name='product'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<slug:slug>/edit/', views.edit_product, name='edit_product'),
    path('product/<slug:slug>/delete/', views.delete_product, name='delete_product'),

]