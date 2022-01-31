from django.shortcuts import render


def home_page(request):
    return render(request, 'shop/home/home.html')