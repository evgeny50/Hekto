from django.urls import path

from interface.views import shop
from interface.views.shop import categories_view, detail_category, home_page, detail_view_product, create_product, \
    edit_product, delete_product, get_price_prediction, get_property_values

urlpatterns = [
    path('category/', categories_view, name='categories'),
    path('category/<slug:slug>/', detail_category, name='category'),
    path('', home_page, name='shop_home-page'),
    path('product/create/', create_product, name='create_product'),
    path('product/<slug:slug>/edit/', edit_product, name='edit_product'),
    path('product/<slug:slug>/delete/', delete_product, name='delete_product'),
    path('predict-price/', get_price_prediction, name='predict_price'),
    path('<slug:slug>/', detail_view_product, name='product'),
    path('api/property-values/', get_property_values, name='property-values'),

]