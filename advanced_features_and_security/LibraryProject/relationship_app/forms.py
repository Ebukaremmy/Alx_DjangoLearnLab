from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Registration form using built-in UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
