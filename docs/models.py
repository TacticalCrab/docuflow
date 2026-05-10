from django.db import models
from django.conf import settings

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, help_text="Markdown content lives here")

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        self.title
    
    class Meta:
        ordering = ['-updated_at']
