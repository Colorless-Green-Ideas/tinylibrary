from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=1024)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=1024)
    
    def get_absolute_url(self):
        return reverse('tinylibrary:book-detail', args=[self.pk])