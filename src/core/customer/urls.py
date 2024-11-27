from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    path('login/', views.user_login, name='customer_login'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('logout/', auth_view.LogoutView.as_view(), name='customer_logout'),
    path('register/', views.user_register, name='customer_register'),
    path('register_seller/', views.seller_register, name='seller_register'),
    path('change_password/', views.PasswordChange.as_view(), name='change_password'),
    path('change_password/done/', views.PasswordChangeDone.as_view(), name='change_password_done'),
    path('reset_password/', views.ResetPassword.as_view(), name='reset_password'),
    path('reset_password/done/', views.ResetPasswordDone.as_view(), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='reset_password_confirm'),
    path('reset/done/', views.PasswordResetConfirmDone.as_view(), name='reset_password_confirm_done'),
    path('seller_manage_products/', views.PasswordResetConfirmDone.as_view(), name='seller_manage_products'),
    path('seller_orders/', views.PasswordResetConfirmDone.as_view(), name='seller_orders'),
    path('edit_profile/', views.PasswordResetConfirmDone.as_view(), name='edit_profile'),
    path('seller_statistics/', views.PasswordResetConfirmDone.as_view(), name='seller_statistics')
]
