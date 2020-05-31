from .models import RestBoard
from django import forms

class RestBoardForm(forms.ModelForm):
    class Meta:
        model = RestBoard
        fields = [ 'title', 'img', 'text' ]
