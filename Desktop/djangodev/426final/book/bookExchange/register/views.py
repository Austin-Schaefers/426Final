from django.shortcuts import render
from . import forms

def register(request):
    form = forms.rForm()
    return render(request, 'register/register.html',{'form':form})