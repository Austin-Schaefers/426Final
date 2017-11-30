from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    render(request, 'login/login.html', {})