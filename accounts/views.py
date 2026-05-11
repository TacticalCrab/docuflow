from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import DocuFlowRegistrationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest


def register_view(request: WSGIRequest):
    if request.method == "POST":
        form = DocuFlowRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("accounts:login", permanent=True)
    else:
        form = DocuFlowRegistrationForm()
    
    return render(request, 'register.html', {
        "form": form
    })


def login_view(request: WSGIRequest):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        
            return redirect("accounts:profile")
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})


@login_required
def profile_view(request: WSGIRequest):
    return render(request, "profile.html")
