from django.shortcuts import render


def first_level(request):
    return render(request, 'first_level/first_level.html')