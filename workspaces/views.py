from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from workspaces.models import Workspace, WorkspaceMember, WorkspaceInvitation
from django.contrib import messages

@login_required
def workspace_dashboard_view(request: HttpRequest, slug: str):
    workspace = get_object_or_404(Workspace, slug=slug)

    if not workspace.is_member(request.user):
        return redirect("root")

    documents = workspace.documents.all().order_by("-updated_at")

    context = {
        "workspace": workspace,
        "documents": documents,
        "is_owner": workspace.is_owner(request.user)
    }

    return render(request, "dashboard.html", context)

@login_required
def create_workspace(request: HttpRequest):
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

        redirect("workspaces:workspace_dashboard", slug=workspace.slug)

    return render(request, "create_workspace.html")

@login_required
def send_invite(request: HttpRequest, slug):
    workspace = get_object_or_404(Workspace, slug=slug)

    if not workspace.memberships.filter(user=request.user, role="owner").exists():
        messages.error(request, "Only owners can invite members.")
        return redirect("workspaces:workspace_dashboard", slug=slug)
    
    if request.method == "POST":
        email = request.POST.get('email')
        role = request.POST.get("role", 'reader')

        if workspace.memberships.filter(user__email=email).exists():
            messages.error(request, "This user is already a member.")
            return redirect("workspaces:workspace_dashboard", slug=slug)
    
    invite = WorkspaceInvitation.objects.create(
        workspace=workspace,
        email=email,
        role=role,
        invited_by=request.user
    )

    return redirect('workspaces:workspace_dashboard', slug=invite.workspace.slug)

@login_required
def respond_to_invite(request: HttpRequest, invite_id):
    invite: WorkspaceInvitation = get_object_or_404(WorkspaceInvitation, id=invite_id, email=request.user.email, accepted=False)

    if request.method == "POST":
        action = request.POST.get('action')
        if action == "accept":
            WorkspaceMember.objects.get_or_create(
                workspace=invite.workspace,
                user=request.user,
                role=invite.role
            )

            invite.accepted = True
            invite.save()
            messages.success(request, f"Joined {invite.workspace.name}!")
            return redirect("workspaces:workspace_dashboard", slug=invite.workspace.slug)
    
    elif action == "decline":
        invite.delete()
        messages.info(request, "Invitation declined.")
    
    return redirect("root")