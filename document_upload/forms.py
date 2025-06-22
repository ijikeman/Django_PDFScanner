from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']
        labels = {
            'name': 'ファイル名',
            'file': 'ファイル',
        }
