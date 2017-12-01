from django import forms
from register.models import Student

class rForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
