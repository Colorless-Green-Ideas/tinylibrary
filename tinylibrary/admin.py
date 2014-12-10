from django.contrib import admin

# Register your models here.
from tinylibrary.models import Book

admin.site.register((Book))