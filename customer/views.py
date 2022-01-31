from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import UserAuth


def user_login(request):
    if request.method == "POST":
        form = UserAuth(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop_home-page')
    else:
        form = UserAuth()
    context = {'form': form}
    return render(request, 'customer/login.html', context)