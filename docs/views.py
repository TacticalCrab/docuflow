from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from django.core.handlers.wsgi import WSGIRequest

@login_required
def edit_document_view(request: WSGIRequest, pk=None):
    if pk:
        doc = get_object_or_404(Document, pk=pk, owner=request.user)
    else:
        doc = Document(owner=request.user)

    if request.method == "POST":
        doc.title = request.POST.get('title')
        doc.content = request.POST.get('content', '')
        doc.save()
        return redirect("docs:edit_document", pk=doc.pk)

    return render(request, "markdown_editor.html", {"document": doc})

@login_required
def dashboard_view(request: WSGIRequest):
    documents = request.user.documents.all().order_by("-updated_at")
    return render(request, "dashboard.html", {"documents": documents})