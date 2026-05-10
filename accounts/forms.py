from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DocuFlowRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Required")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email"
        )
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if "admin" in username.lower():
            raise forms.ValidationError("Username cannot contain the word \"admin\"")

        return username