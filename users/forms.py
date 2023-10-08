from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm password",
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
