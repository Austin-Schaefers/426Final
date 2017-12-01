from django.db import models


# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=12, unique=False)
    lastName = models.CharField(max_length=12, unique=False)
    password = models.CharField(max_length=12, unique=False)
    email = models.EmailField(default="")
    school = models.CharField(max_length=20, unique=False)


class Book(models.Model):
    sid = models.ForeignKey(Student)
    ISBN = models.IntegerField(max_length=13)
    title = models.CharField(max_length=25)
    edition = models.IntegerField()

class Exchange(models.Model):
    eid = models.IntegerField(max_length=12, unique=True)


