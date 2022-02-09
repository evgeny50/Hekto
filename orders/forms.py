from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'order-form-email',
                                             'placeholder': 'Email or mobile phone number'}),
            'first_name': forms.TextInput(attrs={'class': 'order-form-name',
                                                 'placeholder': 'First name (optional)'}),
            'last_name': forms.TextInput(attrs={'class': 'order-form-name',
                                                 'placeholder': 'First name (optional)'}),
            'address': forms.TextInput(attrs={'class': 'order-form-email address',
                                                 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'order-form-name',
                                                'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'order-form-name city',
                                                'placeholder': 'Postal Code'}),

        }