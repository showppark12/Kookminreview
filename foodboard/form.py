from django import forms
from .models import FoodBoard

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodBoard
        fields = ['title', 'img', 'text']