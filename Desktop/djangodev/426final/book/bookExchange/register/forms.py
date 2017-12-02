from django import forms
from django.contrib.auth.models import User
from register.models import Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = Student
        fields = ('Username','firstname','surname', 'email', 'password','school')

