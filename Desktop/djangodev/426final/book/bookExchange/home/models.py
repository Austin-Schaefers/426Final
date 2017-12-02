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
    ISBN  = models.IntegerField()
    title = models.CharField(max_length=40)

""" Listing Table

A listing of a book by a student.
Field type indicates whether is book the student is listing is one he/she wants(W) or is giving(G).
"""
class Listing(models.Model):
    TYPES = (
        ('W', 'Want'),
        ('G', 'Give'),
    )
    lid  = models.IntegerField(unique=True, primary_key=True)
    sid  = models.ForeignKey(Student)
    bid  = models.ForeignKey(Book)
    type = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField(auto_now_add=True)
    open = models.BooleanField(default=True)

""" Exchange Table

An exchange of books between two students.
Field bid1 represents the book sid1 is giving away and vice versa with bid2/sid2
"""
class Exchange(models.Model):
    eid  = models.IntegerField(unique=True, primary_key=True)
    sid1 = models.ForeignKey(Student)
    bid1 = models.ForeignKey(Book)
    sid2 = models.ForeignKey(Student)
    bid2 = models.ForeignKey(Book)
    date = models.DateField(auto_now_add=True)
