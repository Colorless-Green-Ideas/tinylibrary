from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

import csv
import json

from .models import Book, Person
from .forms import BookForm, PersonForm, ImportCSVForm
# Create your views here.

class index(ListView):
    model = Book

class book(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()

class CreateBook(CreateView):
    form_class = BookForm
    model = Book

class UpdateBook(UpdateView):
    form_class = BookForm
    model = Book

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy("tinylibrary:book-home")

class CreatePerson(CreateView):
    form_class = PersonForm
    model = Person
    success_url = reverse_lazy("tinylibrary:book-home")

class HomeView(TemplateView):
    template_name = "base.html"

class QuaggaTest(TemplateView):
    template_name = "tinylibrary/quagga_test.html"

class CreateBookFromISBN(CreateView):
    model = Book
    fields = ['isbn']

class ImportCSV(FormView):
    form_class = ImportCSVForm
    template_name = "tinylibrary/import.html"
    success_url = reverse_lazy("tinylibrary:book-home")
    def form_valid(self, form):
        if form.is_valid():
            csv_data = self.request.FILES['file']
            for row in csv.DictReader(csv_data):
                held_by = form.cleaned_data['held_by']
                b = Book.from_gr_csv_dict(row, held_by)
                print(b)
                b.save()
        return super(ImportCSV, self).form_valid(form)

@csrf_exempt
def webhook_payload(request):
    if request.CONTENT_TYPE != "application/json":
        return HttpResponse(status=500)
    data = json.loads(request.body)
    event_type = request.META['X-Github-Event']
    print(data)
    # print payload
    return HttpResponse(status=200)