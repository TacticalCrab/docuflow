from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'workspaces'

urlpatterns = [
    path("create_workspace/", views.create_workspace, name="create_workspace"),
    path("<slug:slug>/", views.workspace_dashboard_view, name="workspace_dashboard")
]
