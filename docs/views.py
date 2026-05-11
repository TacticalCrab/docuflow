from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from workspaces.models import Workspace
from django.core.handlers.wsgi import WSGIRequest

@login_required
def edit_document_view(request: WSGIRequest, pk=None):
    if pk:
        doc = get_object_or_404(Document, pk=pk)
    else:
        doc = Document()

    context = {
        "document": doc,
        "can_edit": doc.workspace.can_edit(request.user),
        "workspace": doc.workspace
    }

    return render(request, "markdown_editor.html", context)


@login_required
def create_document(request: WSGIRequest, slug):
    workspace = get_object_or_404(Workspace, slug=slug)

    if not workspace.can_edit(request.user):
        return redirect("docs:dashboard")

    new_doc = Document.objects.create(
        title = request.POST.get('title', "Untitled"),
        workspace = workspace,
        creator = request.user
    )

    return redirect("docs:edit_document", pk=new_doc.pk)

@login_required
def save_document(request: WSGIRequest, pk):
    doc = get_object_or_404(Document, pk=pk)
    workspace = doc.workspace

    if not workspace.can_edit(request.user):
        messages.error(request, "You only have 'Reader' access to this workspace.")
        return redirect("docs:dashboard")

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get("content")

        # 3. Validation
        if not title:
            messages.error(request, "Title cannot be empty.")
            return redirect("docs:edit_document", pk=doc.pk)
        
        doc.title = title
        doc.content = content
        doc.save()

        return redirect("docs:edit_document", pk=doc.pk)

    return redirect("docs:edit_document", pk=doc.pk)
