from django.shortcuts import render

# Create your views here.
def home(request):
    myDict = {"insert_me": "text"}
    return render(request,"home/home.html", myDict)

