from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    path('login/', views.user_login, name='customer_login'),
    path('logout/', auth_view.LogoutView.as_view(), name='customer_logout'),
    path('register/', views.user_register, name='customer_register'),
    path('change_password/', views.PasswordChange.as_view(), name='change_password'),
    path('change_password/done/', views.PasswordChangeDone.as_view(), name='change_password_done'),
    path('reset_password/', views.ResetPassword.as_view(), name='reset_password'),
    path('reset_password/done/', views.ResetPasswordDone.as_view(), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='reset_password_confirm'),
    path('reset/done/', views.PasswordResetConfirmDone.as_view(), name='reset_password_confirm_done')
]
