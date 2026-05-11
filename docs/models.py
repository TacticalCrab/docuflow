from django.db import models
from django.contrib.auth.models import User
from workspaces.models import Workspace

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, help_text="Markdown content lives here")

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.title
    
    class Meta:
        ordering = ['-updated_at']
