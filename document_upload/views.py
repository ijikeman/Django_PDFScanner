from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_document(request):
    # Post Method: Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) # form.pyのDocumentFormを使用
        if form.is_valid(): # Validate the form
            form.save() # save the uploaded file
            return render(request, 'upload.html', {'form': form})
    # Get Method: Display the upload form
    else:
        form = DocumentForm() # form.pyのDocumentFormを使用
    return render(request, 'document_upload/upload.html', {'form': form}) # /templates/document_upload/upload.htmlを表示
