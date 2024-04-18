from django import forms
from .models import text

class textForm(forms.ModelForm):
    class  Meta:
        model = text
        fields = ('content',)
        labels = {
            'content': '',
        }
        widgets = {''
            'content': forms.Textarea(attrs={
                'placeholder': "Enter your description here!",
                'class': 'form-control'}),
        }
