from django.shortcuts import render
from . import forms
from django.views.generic.edit import FormView
from . import models
from .models import Book
from django.http import HttpResponse
import json
# Create your views here.
def home(request):
    session_language = 'en'
    request.session['lang'] = session_language


    return render(request,"home/home.html", {'session_language':session_language})

class AutoCompleteView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        bookname = data.get("term")
        if bookname:
            books = Book.objects.filter(title__contains= bookname)
        else:
            books = Book.objects.all()

        results = []
        for book in books:
            book_json = {}
            book_json['id'] = book.id
            book_json['label'] = book.title
            book_json['value'] = book.title
            results.append(book_json)
            data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)