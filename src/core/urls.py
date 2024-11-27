from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('core.payment.urls')),
    path('cart/', include('core.cart.urls')),
    path('', include('core.shop.urls')),
    path('accounts/', include('core.customer.urls')),
    path('orders/', include('core.orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
