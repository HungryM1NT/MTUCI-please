from django.contrib import admin
from django.urls import path
from first_level.views import first_level

app_name = 'first_level'

urlpatterns = [
    path('', first_level, name='first_level'),
]