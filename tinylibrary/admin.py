from django.contrib import admin

# Register your models here.
from tinylibrary.models import Book, Person

admin.site.register((Book, Person))