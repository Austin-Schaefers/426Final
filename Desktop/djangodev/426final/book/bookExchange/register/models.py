from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=12, unique=False)
    lastName = models.CharField(max_length=12, unique=False)
    password = models.CharField(max_length=12, unique=False)
    school = models.CharField(max_length=20, unique=False)
