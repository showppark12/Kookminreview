from django import forms
from .models import Blog

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodForm
        fields = ['title', 'pub_date', 'img', 'text']