from django.shortcuts import render
from . import forms

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

