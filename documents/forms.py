from django import forms
from .models import Document
from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']
        labels = {
            'name': 'ファイル名',
            'file': 'ファイル',
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.name.split('.')[-1].lower() != 'pdf':
            raise ValidationError('PDFファイルのみアップロードできます。')
        return file

class DocumentDeleteForm(forms.Form):
    name = forms.CharField(label='ファイル名')

    # ファイルが存在するか確認するメソッド
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Document.objects.get(name=name)
        except Document.DoesNotExist:
            raise ValidationError('指定されたファイル名のドキュメントは存在しません。')
        return name
