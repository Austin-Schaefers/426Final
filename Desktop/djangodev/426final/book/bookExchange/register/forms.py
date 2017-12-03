from django import forms
from django.contrib.auth.models import User
from register.models import Student, studentSchool

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')

class schoolForm(forms.ModelForm):
    class Meta():
        model = studentSchool
        fields = ('school',)