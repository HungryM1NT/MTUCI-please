from django.shortcuts import render
from users.forms import UserLoginForm, UserRegistrationForm


def index(request):
    context = {
        'login_form': UserLoginForm(),
        'registration_form': UserRegistrationForm(),
    }
    return render(request, 'main_page/index.html', context)
