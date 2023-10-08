from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
        else:
            registration_form = UserRegistrationForm()
            context = {
                'login_form': login_form,
                'registration_form': registration_form
            }
            return render(request, 'main_page/index.html', context)
    return HttpResponseRedirect(reverse('index'))


def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()
        else:
            login_form = UserLoginForm()
            context = {
                'login_form': login_form,
                'registration_form': registration_form
            }
            return render(request, 'main_page/index.html', context)
    return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))