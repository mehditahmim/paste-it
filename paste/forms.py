
from django import forms
from .models import Paste

class CreatePasteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=150, required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 15}), required=True)
    

    class Meta:
        model = Paste
        fields = ['title', 'text']

class EditPasteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=150, required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 15}), required=True)

    class Meta:
        model = Paste
        fields = ['title', 'text']  

