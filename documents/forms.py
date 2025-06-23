from django import forms
from .models import Document
from django.core.exceptions import ValidationError

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file', 'page_numbers']
        labels = {
            'name': 'ファイル名',
            'file': 'ファイル',
            'page_numbers': 'ページ番号',
        }

    def clean_page_numbers(self):
        page_numbers_str = self.cleaned_data.get('page_numbers')
        if not page_numbers_str:
            return []
        try:
            if '-' in page_numbers_str:
                start, end = map(int, page_numbers_str.split('-'))
                if start > end:
                    raise ValidationError("開始ページ番号は終了ページ番号より小さい必要があります。")
                return list(range(start, end + 1))
            elif ',' in page_numbers_str:
                return [int(x) for x in page_numbers_str.split(',')]
            else:
                return [int(page_numbers_str)]
        except ValueError:
            raise ValidationError("ページ番号は整数で入力してください。")

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
