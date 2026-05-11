from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workspaces/', include("workspaces.urls")),
    path("", include("accounts.urls")),
    path("", include("docs.urls")),
    path("", views.root_redirect)
]
