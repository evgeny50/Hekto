from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserAuth(AuthenticationForm):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(
                                   attrs={'class': 'form__username',
                                          'placeholder': 'Email Address'}
                               ))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form__username form__password',
                                          'placeholder': 'Password'}
                               ))