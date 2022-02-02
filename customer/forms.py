from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput
        (attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
