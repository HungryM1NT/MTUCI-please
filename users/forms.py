from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        # Параметры будущей формы логина
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        # Параметры будущей формы пароля
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        # Параметры будущей формы логина
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        # Параметры будущей формы пароля
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        # Параметры будущей формы пароля х2
    }))


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']