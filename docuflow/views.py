from django.shortcuts import redirect
from django.http import HttpRequest

def root_redirect(request: HttpRequest):
    first_membership = request.user.memberships.first()
    workspace = first_membership.workspace

    if request.user.is_authenticated:
        return redirect('workspaces:workspace_dashboard', slug=workspace.slug)
    else:
        return redirect('accounts:login')
