from django.shortcuts import render
from django.shortcuts import redirect


def first_level(request):
    return redirect('http://localhost:5173/')