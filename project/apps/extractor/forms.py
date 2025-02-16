from django import forms
from .models import PDFDocument

class PDFUploadForm(forms.ModelForm):
    page_numbers = forms.CharField(
        required=False, 
        help_text="例: 1,3,5 (抽出したいページをカンマ区切りで指定)"
    )

    class Meta:
        model = PDFDocument
        fields = ('file', 'page_numbers')

    def clean_page_numbers(self):
        data = self.cleaned_data.get("page_numbers", "")
        if data:
            try:
                return [int(num.strip()) for num in data.split(",") if num.strip().isdigit()]
            except ValueError:
                raise forms.ValidationError("ページ番号はカンマ区切りの整数で入力してください。")
        return []
