from django.urls import reverse
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=1024)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=1024)
    held_by = models.ForeignKey('Person', on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('tinylibrary:book-detail', args=[self.pk])
    @classmethod
    def from_gr_csv_dict(cls, data, held_by):
        return cls(title=data['title'], author=data['authors'], isbn=data["isbn13"], held_by=held_by)
    def __unicode__(self):
        return  u"'{}' - {}  Held by: {}".format(self.title, self.author, self.held_by)

class Person(models.Model):
    name = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.name