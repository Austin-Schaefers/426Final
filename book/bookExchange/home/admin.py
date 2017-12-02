from django.contrib import admin
from home.models import Student, Book, Listing, Exchange

# Register your models here.
#remember to make superuser for everybody in the group pass: pass user: name
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Listing)
admin.site.register(Exchange)