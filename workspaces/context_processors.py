from .models import Workspace
from django.http import HttpRequest

def user_workspaces(request: HttpRequest):
    if request.user.is_authenticated:
        return {
            'my_workspaces': Workspace.objects.filter(memberships__user=request.user)
        }
    else:
        return {}