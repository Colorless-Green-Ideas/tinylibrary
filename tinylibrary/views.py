from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import json

from models import Book, Person
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

class CreatePerson(CreateView):
    model = Person
    success_url = reverse_lazy("tinylibrary:book-home")

@csrf_exempt
def webhook_payload(request):
    print request.body
    # print payload
    return HttpResponse(status=200)