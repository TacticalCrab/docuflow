from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Workspace(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_user_role(self, user):
        membership = self.memberships.filter(user=user).first()
        return membership.role if membership else None

    def is_member(self, user):
        return self.memberships.filter(user=user).exists()

    def can_edit(self, user):
        role = self.get_user_role(user)
        return role in ["owner", "editor"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WorkspaceMember(models.Model):
    ROLE_CHOICES = (
        ("owner", "Owner"),
        ("editor", "Editor"),
        ("reader", "reader")
    )

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="reader")

    class Meta:
        unique_together = ('workspace', 'user')
