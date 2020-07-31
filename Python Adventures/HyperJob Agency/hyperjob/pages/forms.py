from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
        model = 'signup'

class LoginForm(AuthenticationForm):
    class Meta:
        app_label = 'login'
        fields = [
            'username',
            'password'
        ]