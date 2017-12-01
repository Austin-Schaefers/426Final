import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bookExchange.settings')

import django
django.setup()

import random
from register.models import Student, Book
from faker import Faker

fakegen = Faker()

