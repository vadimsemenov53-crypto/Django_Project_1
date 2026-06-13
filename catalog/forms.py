from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from .validators import INVALID_WORDS


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in INVALID_WORDS:
            if word in name.lower():
                raise ValidationError('В названии продукта используются запрещенные слова.')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        for word in INVALID_WORDS:
            if word in description.lower():
                raise ValidationError('В описании продукта используются запрещенные слова.')

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')

        return price