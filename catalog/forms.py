from django.forms import ModelForm, BooleanField
from catalog.models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        name_lower = name.lower()
        description_lower = description.lower()


        for word in self.forbidden_words:
            if word in name_lower:
                self.add_error('name', f"Название содержит запрещенное слово: '{word}'.")

        for word in self.forbidden_words:
            if word in description_lower:
                self.add_error('description', f"Описание содержит запрещенное слово: '{word}'.")

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена товара не может быть отрицательной, проверьте цену')
        return price