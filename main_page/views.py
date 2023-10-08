from django.shortcuts import render
from main_page.models import Person


def index(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'main_page/testindex.html', context)