from django import forms
from .models import FoodBoard, FoodComment

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodBoard
        fields = [ 'title', 'img', 'text' ]

class FoodCommentForm(forms.ModelForm):
    class Meta:
        model = FoodComment
        fields = [ 'text' ]