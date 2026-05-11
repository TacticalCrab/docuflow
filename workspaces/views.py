from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from workspaces.models import Workspace, WorkspaceMember


@login_required
def workspace_dashboard_view(request: WSGIRequest, slug: str):
    workspace = get_object_or_404(Workspace, slug=slug)

    if not workspace.is_member(request.user):
        return redirect("root")

    documents = workspace.documents.all().order_by("-updated_at")

    context = {
        "workspace": workspace,
        "documents": documents
    }

    return render(request, "dashboard.html", context)

@login_required
def create_workspace(request: WSGIRequest):
    if request.method == "POST":
        workspace_name = request.POST.get("name")

        workspace = Workspace.objects.create(
            name=workspace_name
        )

        WorkspaceMember.objects.create(
            workspace=workspace,
            user=request.user,
            role="owner"
        )

        redirect(f"workspaces:workspace_dashboard {workspace.slug}")

    return render(request, "create_workspace.html")