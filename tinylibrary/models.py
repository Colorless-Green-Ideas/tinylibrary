import logging
from django.urls import reverse
from django.db import models
from .util import fetch_data
logger = logging.getLogger(__name__)

class Book(models.Model):
    title = models.CharField(max_length=1024)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=1024)
    lcc_section = models.CharField(max_length=10, null=True, blank=True)
    ddc_number = models.CharField(max_length=10, null=True, blank=True)
    held_by = models.ForeignKey('Person', on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('tinylibrary:book-detail', args=[self.pk])
    @classmethod
    def from_gr_csv_dict(cls, data, held_by):
        logger.info(data)
        if len(data["ISBN13"]) > 13 and data["ISBN13"].startswith('="'):
            isbn13 = data["ISBN13"][2:-1]
        else:
            isbn13 = data["ISBN13"]
        return cls(title=data['Title'], author=data['Author'], isbn=isbn13, held_by=held_by)
    @classmethod
    def from_isbn(cls, isbn):
        data = fetch_data(isbn)
        return cls(isbn=isbn)

    def __str__(self):
        return  "'{}' - {}  Held by: {}".format(self.title, self.author, self.held_by)

class Person(models.Model):
    name = models.CharField(max_length=1024)
    def __str__(self):
        return self.name