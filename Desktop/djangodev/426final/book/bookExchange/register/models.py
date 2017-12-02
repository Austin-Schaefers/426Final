from django.db import models

""" Student Table

Standard db representation of a student
"""
class Student(models.Model):
    sid    = models.IntegerField(unique=True, primary_key=True)
    fname  = models.CharField(max_length=20, unique=False)
    lname  = models.CharField(max_length=20, unique=False)
    pword  = models.CharField(max_length=40, unique=False)
    email  = models.EmailField(default="")
    school = models.CharField(max_length=40, unique=False)

""" Book Table

Standard db representation of a book
"""
class Book(models.Model):
    bid   = models.IntegerField(unique=True, primary_key=True)
    isbn  = models.IntegerField()
    title = models.CharField(max_length=40)
