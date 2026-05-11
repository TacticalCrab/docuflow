from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'workspaces'

urlpatterns = [
    path("create_workspace/", views.create_workspace, name="create_workspace"),
    path("<slug:slug>/", views.workspace_dashboard_view, name="workspace_dashboard"),
    path("send_invite/<slug:slug>", views.send_invite, name="send_invite"),
    path("respond_to_invite/<int:invite_id>", views.respond_to_invite, name="respond_to_invite")
]
