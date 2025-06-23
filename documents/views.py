from django.shortcuts import render, redirect
from .forms import DocumentForm
import os

def upload(request):
    # Post Method: Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) # form.pyのDocumentFormを使用
        if form.is_valid(): # Validate the form
            form.save() # save the uploaded file
            return render(request, 'upload.html', {'form': form})
    # Get Method: Display the upload form
    else:
        form = DocumentForm() # form.pyのDocumentFormを使用
    return render(request, 'documents/upload.html', {'form': form}) # /templates/document_upload/upload.htmlを表示

def list(request):
    documents_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload_files')
    files = os.listdir(documents_dir)
    return render(request, 'documents/list.html', {'files': files})
