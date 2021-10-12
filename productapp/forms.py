from django import forms
from django.forms import ModelForm

from productapp.models import Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'market_name', 'head_image']

