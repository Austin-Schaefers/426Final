from django.db import models
from django.contrib.auth.models import User

""" Student Table

Standard db representation of a student
"""
class Student(models.Model):
    #Django User automatically creates password,email,firstname,surname, username
    user = models.OneToOneField(User)

    #additional fields
    sid    = models.IntegerField(unique=True, primary_key=True)
    school = models.CharField(max_length=40, unique=False)

    def _str_(self):
        return self.user.username


""" Book Table

Standard db representation of a book
"""
class Book(models.Model):
    bid   = models.IntegerField(unique=True, primary_key=True)
    isbn  = models.IntegerField()
    title = models.CharField(max_length=40)
