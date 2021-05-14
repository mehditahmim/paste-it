
from django import forms
from .models import Paste

class CreatePasteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=150, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    

    class Meta:
        model = Paste
        fields = ['title', 'text']

class EditPasteForm(forms.ModelForm):

    class Meta:
        model = Paste
        fields = ['title', 'text']  

