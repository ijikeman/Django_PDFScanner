from django.shortcuts import render, redirect
from .forms import DocumentForm, DocumentDeleteForm
from .models import Document
import os

def upload(request):
    # Post Method: Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES) # form.pyのDocumentFormを使用
        if form.is_valid(): # Validate the form
            form.save() # models.pyでDocumentが定義されているため、save()メソッドで./upload_files/に保存される
            return render(request, 'documents/upload.html', {'form': form})

    # Get Method: Display the upload form
    else:
        form = DocumentForm() # form.pyのDocumentFormを使用
    return render(request, 'documents/upload.html', {'form': form}) # /templates/document_upload/upload.htmlを表示

def list(request):
    documents = Document.objects.all() # Documentオブジェクトのすべてを格納
    form = DocumentDeleteForm()
    if request.method == 'POST':
        selected_documents = request.POST.getlist('delete')
        print("POST request received") # debug print
        print(f"selected_documents: {selected_documents}") # debug print selected_documents
        for doc_id in selected_documents:
            print(f"doc_id: {doc_id}") # debug print doc_id
            try:
                document = Document.objects.get(pk=doc_id)
                print(f"document: {document}") # debug print document
                document.delete()
            except Document.DoesNotExist:
                print(f"Document with id '{doc_id}' does not exist.") # debug print error message
                pass  # Handle the case where the document doesn't exist
        return redirect('documents:list')  # Redirect to the list view
    return render(request, 'documents/list.html', {'documents': documents, 'form': form}) # list.htmlでdocumentsオブジェクトを表示
