import os
from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFDocument
import PyPDF2
from modules import PdfReader

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_instance = form.save()
            pdf_path = pdf_instance.file.path
            page_numbers = form.cleaned_data.get('page_numbers', [])  # 取得
            print("Extracted page_numbers:", page_numbers)  # デバッグ用
            reader = PdfReader(pdf_instance.file.path, page_numbers) # PdfReaderを使うように改変
            text = reader.pdfplumber()
            return render(request, 'extractor/result.html', {'text': text})
        else:
            print("Form errors:", form.errors)  # ここでエラー内容を確認！
    else:
        form = PDFUploadForm()

    return render(request, 'extractor/upload.html', {'form': form})
