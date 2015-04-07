from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import json

from models import Book, Person
from forms import BookForm, PersonForm
# Create your views here.

class index(ListView):
    model = Book

class book(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()

class CreateBook(CreateView):
    form_class = BookForm
    model = Book
    fields = '__all__'

class UpdateBook(UpdateView):
    form_class = BookForm
    fields = '__all__'
    model = Book

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy("tinylibrary:book-home")

class CreatePerson(CreateView):
    form_class = PersonForm
    model = Person
    success_url = reverse_lazy("tinylibrary:book-home")

@csrf_exempt
def webhook_payload(request):
    if request.CONTENT_TYPE != "application/json":
        return HttpResponse(status=500)
    data = json.loads(request.body)
    event_type = request.META['X-Github-Event']
    print data
    # print payload
    return HttpResponse(status=200)