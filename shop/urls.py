from django.urls import path

from . import views


urlpatterns = [
    path('category/', views.categories_view, name='categories'),
    path('category/<slug:slug>/', views.detail_category, name='category'),
    path('', views.home_page, name='shop_home-page'),
    path('<slug:slug>/', views.detail_view_product, name='product'),
]