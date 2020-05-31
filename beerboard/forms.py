from .models import BeerBoard
from django import forms

class BeerBoardForm(forms.ModelForm):
    class Meta:
        model = BeerBoard
        fields = [ 'title', 'img', 'text' ]

        