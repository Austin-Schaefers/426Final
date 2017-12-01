from django.shortcuts import render
from . import forms

# Create your views here.
def login(request):
    myDict = {"insert_me": "klwemlwemdwe"}
    return render(request, 'login/login.html', myDict)