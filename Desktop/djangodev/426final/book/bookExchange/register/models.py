from django.db import models
from django.contrib.auth.models import User

""" Student Table

Standard db representation of a student
"""
class Student(models.Model):
    #Django User automatically creates password,email,firstname,surname, username
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional fields
    sid    = models.IntegerField(unique=True, primary_key=True)
    fname  = models.CharField("first name", max_length=20, unique=False, default="John")
    lname  = models.CharField("last name", max_length=20, unique=False, default="Smith")
    pword  = models.CharField("password", max_length=40, unique=False, default="")
    email  = models.EmailField("email address", default="")




    def _str_(self):
        return self.user.username

class studentSchool(models.Model):
    school = models.CharField("school", max_length=40, unique=False, default="")

""" Book Table

Standard db representation of a book
"""
class Book(models.Model):
    ISBN  = models.IntegerField(default="")
    title = models.CharField(max_length=40, default="")
