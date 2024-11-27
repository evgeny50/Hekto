from django import forms
from .models import Product, PropertyValue, PropertyKey, MONTH_CHOICES


class ProductForm(forms.ModelForm):
    # Поля для свойств и значений
    property_key = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="Свойство 1",
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'fetchValues(this.value)'})
    )
    property_value = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="Значение",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    property_key_2 = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="Свойство 2",
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'fetchValues(this.value)'})
    )
    property_value_2 = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="Значение",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = [
            'name', 'article', 'description', 'price', 'category', 'tags', "photo", "photo_2", 'photo_3', 'photo_4',
            'stock'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'article': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_4': forms.FileInput(attrs={'class': 'form-control'}),
        }
        exclude = ["property_key",
"property_value",
"property_key_2",
"property_value_2",]
    def clean_price(self):
        """Валидация для поля цены, чтобы оно было больше нуля."""
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля.")
        return price

    def clean_stock(self):
        """Валидация для поля количества на складе, чтобы оно было неотрицательным."""
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Количество на складе не может быть отрицательным.")
        return stock

    # def clean(self):
    #     """Проверка, что оба свойства не одинаковые."""
    #     cleaned_data = super().clean()
    #     property_key = cleaned_data.get('property_key')
    #     property_key_2 = cleaned_data.get('property_key_2')
    #
    #     if property_key == property_key_2:
    #         raise forms.ValidationError("Свойства 1 и 2 не могут быть одинаковыми.")
    #
    #     return cleaned_data
