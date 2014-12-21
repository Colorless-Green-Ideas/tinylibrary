from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Book
# Create your views here.

class index(ListView):
    model = Book

class book(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()

class CreateBook(CreateView):
    model = Book

class UpdateBook(UpdateView):
    model = Book

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy("tinylibrary:book-home")