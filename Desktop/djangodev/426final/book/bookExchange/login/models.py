from django.db import models

""" Student Table

Standard db representation of a student
"""
class Student(models.Model):
    sid    = models.IntegerField(max_length=12, unique=True, primary_key=True)
    fname  = models.CharField(max_length=20, unique=False)
    lname  = models.CharField(max_length=20, unique=False)
    pword  = models.CharField(max_length=40, unique=False)
    email  = models.EmailField(default="")
    school = models.CharField(max_length=40, unique=False)


