from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from models import Book
# Create your views here.

class index(ListView):
    model = Book

class book(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()

class CreateBook(CreateView):
    model = Book
    