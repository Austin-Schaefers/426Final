from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    myDict = {"insert_me": "text"}
    return render(request,"home/home.html", myDict)

def ISBNfinder(request):
    form = forms.homeForm
    return render(request, "home/home.html", form)

