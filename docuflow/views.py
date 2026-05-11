from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect

def root_redirect(request: WSGIRequest):
    if request.user.is_authenticated:
        return redirect('docs:dashboard')
    else:
        return redirect('accounts:login')
