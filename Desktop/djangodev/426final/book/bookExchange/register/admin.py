from django.contrib import admin
from register.models import Student, Book, studentSchool

# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(studentSchool)