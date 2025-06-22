from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_upload:upload_document')  # Redirect to the same page
    else:
        form = DocumentForm()
    return render(request, 'document_upload/upload.html', {'form': form})
