import os
from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFDocument
from modules import PdfReader, TextReplacers, ConvertToCsv

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)

        if form.is_valid():
            pdf_instance = form.save()
            pdf_path = pdf_instance.file.path
            page_numbers = form.cleaned_data.get('page_numbers', [])  # 取得
            divisor = form.cleaned_data.get('divisor', 1)  # デフォルト1
            reader = PdfReader(pdf_instance.file.path, page_numbers) # PdfReaderを使うように改変
            text = reader.pdfplumber()
            replacers = TextReplacers()
            replacers.add('－', '-')
            replacers.add('△', '-')
            replacers.add('※１', '')
            replacers.add('※２', '')
            replacers.add('※３', '')
            replacers.add('※４', '')
            replacers.add('※５', '')
            replacers.add('※６', '')
            replacers.add('※７', '')
            replacers.add('※８', '')
            replacers.add('※９', '')
            replacers.add('※', '')
            replacers.add(',', '')
            replacers.add(',', '')
            replacers.add(' ', ',')
            text = replacers.replace_all(text)
            # 数字を divisor で割り、四捨五入
            processed_text = []
            for line in text:
                parts = line.split(",")  # カンマ区切りで分割
                for i in range(1, len(parts)):  # 最初の要素（文字列）はそのまま
                    try:
                        if parts[i].strip() == "-":  # '-' の場合はそのまま
                            continue
                        parts[i] = str(round(int(parts[i]) / divisor))  # 割り算 & 四捨五入
                    except ValueError:
                        pass  # 数値変換できない場合はスキップ
                processed_text.append(",".join(parts))  # 文字列に戻す
            return render(request, 'extractor/result.html', {'text': processed_text})
        else:
            print("Form errors:", form.errors)  # ここでエラー内容を確認！
    else:
        form = PDFUploadForm()

    return render(request, 'extractor/upload.html', {'form': form})
