from django import forms
from .models import restboard

class BlogForm(forms.ModelForm):
    class Meta:
        model = restboard
        fields = ['title', 'body', 'image']