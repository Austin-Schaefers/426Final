from django.contrib import admin
from home import models

# Register your models here.
#remember to make superuser for everybody in the group pass: pass user: name
admin.site.register(models.Student)
admin.site.register(models.Book)
admin.site.register(models.Listing)
admin.site.register(models.Exchange)