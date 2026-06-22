from django import forms
from .models import Product
from categories.models import Category


class ProductForm(forms.ModelForm):
    image = forms.ImageField(
        label='Фото продукту',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full text-sm text-gray-400 '
                     'file:mr-4 file:py-2 file:px-4 '
                     'file:rounded-lg file:border-0 '
                     'file:text-sm file:font-semibold '
                     'file:bg-indigo-600 file:text-white '
                     'hover:file:bg-indigo-500 '
                     'cursor-pointer',
            'accept': 'image/*',
        }),
    )

    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white focus:border-indigo-500 focus:outline-none',
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white',
                'placeholder': 'Назва продукту ...',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white',
                'placeholder': 'product-name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white',
                'rows': 4,
                'placeholder': 'Опис продукту ...',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white',
                'step': '0.01',
                'placeholder': '0.00',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Product.objects.filter(name=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Продукт з такою назвою вже існує.')
        return name
