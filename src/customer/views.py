from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, views
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserAuth, UserRegisterForm


def user_login(request):
    """
    If the data are received by post method, we check
    the form for validity, and if it is successful, we
    authorize the user and return him to the home page.
    """
    if request.method == "POST":
        form = UserAuth(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop_home-page')
    form = UserAuth()
    context = {'form': form}
    return render(request, 'customer/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop_home-page')
    form = UserRegisterForm()
    return render(request, 'customer/register.html', {'form': form})


class PasswordChange(SuccessMessageMixin, views.PasswordChangeView):
    template_name = 'customer/change_password.html'
    success_url = reverse_lazy('change_password_done')


class PasswordChangeDone(views.PasswordChangeDoneView):
    template_name = 'customer/change_password_done.html'


class ResetPassword(views.PasswordResetView):
    email_template_name = 'customer/email_reset_password.html'
    template_name = 'customer/reset_password.html'
    success_url = reverse_lazy('reset_password_done')


class ResetPasswordDone(views.PasswordResetDoneView):
    template_name = 'customer/reset_password_done.html'


class PasswordResetConfirm(views.PasswordResetConfirmView):
    template_name = 'customer/password_reset_confirm.html'
    success_url = reverse_lazy('reset_password_confirm_done')


class PasswordResetConfirmDone(views.PasswordResetCompleteView):
    template_name = 'customer/password_reset_confirm_done.html'
