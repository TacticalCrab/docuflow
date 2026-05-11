from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Workspace, WorkspaceMember

@receiver(post_save, sender=User)
def create_personal_workspace(sender, instance: User, created, **kwargs):
    if created:
        workspace = Workspace.objects.create(
            name=f"{instance.username}'s Workspace"
        )

        WorkspaceMember.objects.create(
            workspace=workspace,
            user=instance,
            role="owner"
        )