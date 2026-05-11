from .models import Workspace, WorkspaceInvitation
from django.http import HttpRequest

def user_workspaces(request: HttpRequest):
    if request.user.is_authenticated:
        return {
            'my_workspaces': Workspace.objects.filter(memberships__user=request.user)
        }
    else:
        return {}

def user_invitations(request):
    if request.user.is_authenticated:
        return {
            'pending_invites': WorkspaceInvitation.objects.filter(
                email=request.user.email, 
                accepted=False
            )
        }
    return {}