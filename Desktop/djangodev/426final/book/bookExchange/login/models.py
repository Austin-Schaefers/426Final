from django.db import models

""" Student Table

Standard db representation of a student
"""
class Student(models.Model):
    fname  = models.CharField("first name", max_length=20, unique=False, default="John")
    lname  = models.CharField("last name", max_length=20, unique=False, default="Smith")
    pword  = models.CharField("password", max_length=40, unique=False, default="")
    email  = models.EmailField("email address", default="")
    school = models.CharField("school", max_length=40, unique=False, default="")
