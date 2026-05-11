from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path("save_document/<int:pk>", views.save_document, name="save_document"),
    path("edit_document/<int:pk>", views.edit_document_view, name="edit_document"),
    path("create_document/<slug:slug>", views.create_document, name="create_document")
]