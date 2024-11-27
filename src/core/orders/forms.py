# src/core/interface/forms/order_form.py

from django import forms

from core.shop.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'order-form-email',
                'placeholder': 'Email or mobile phone number'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'order-form-name',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'order-form-name',
                'placeholder': 'Last name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'order-form-address',
                'placeholder': 'Address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'order-form-city',
                'placeholder': 'City'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'order-form-postal-code',
                'placeholder': 'Postal Code'
            }),
        }
