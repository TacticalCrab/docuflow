from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path("edit_document/<int:pk>", views.edit_document_view, name="edit_document"),
    path("edit_document/", views.edit_document_view, name="create_document"),
    path("dashboard", views.dashboard_view, name="dashboard")
]