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
    documents = Document.objects.all()
    form = DocumentDeleteForm()
    if request.method == 'POST':
        selected_documents = request.POST.getlist('delete_documents')
        for doc_id in selected_documents:
            try:
                document = Document.objects.get(pk=doc_id)
                document.delete()
            except Document.DoesNotExist:
                pass  # Handle the case where the document doesn't exist
        return redirect('documents:list')  # Redirect to the list view
    return render(request, 'documents/list.html', {'documents': documents, 'form': form})
