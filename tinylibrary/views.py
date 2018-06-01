import csv
import json
import logging
import io

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.views.generic.edit import FormView

from .forms import BookForm, ImportCSVForm, PersonForm
from .models import Book, Person

logger = logging.getLogger(__name__)

class IndexView(ListView):
    model = Book

class DetailBook(DetailView):
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
    template_name = "modern.html"

class HelpView(TemplateView):
    template_name ="tinylibrary/help.html"

class QuaggaTest(TemplateView):
    template_name = "tinylibrary/quagga2.html"

class ButtonsTest(TemplateView):
    template_name = "tinylibrary/buttons.html"

def httpcats(status):
    return redirect("https://http.cat/%s" % status)

class CreateBookFromISBN(CreateView):
    model = Book
    fields = ['isbn', 'held_by']

    def form_valid(self, form):
        logger.info(form.cleaned_data)
        #make the object from isbn
        isbn = form.cleaned_data['isbn']
        if len(isbn) in [7,13]:
            b = Book.from_isbn(isbn)
            b.held_by = form.cleaned_data['held_by']
            b.save()
            return HttpResponseRedirect(reverse_lazy("tinylibrary:book-home"))
        else:
            logger.error("ISBN is non-standard")
            return httpcats(411)


class ImportCSV(FormView):
    form_class = ImportCSVForm
    template_name = "tinylibrary/import.html"
    success_url = reverse_lazy("tinylibrary:book-home")
    def form_valid(self, form):
        if form.is_valid():
            csv_data = self.request.FILES['file']

            if csv_data.multiple_chunks:
                csv_data.seek(0)
                # https://andromedayelton.com/2017/04/25/adventures-with-parsing-django-uploaded-csv-files-in-python3/
                for row in csv.DictReader(io.StringIO(csv_data.read().decode('utf-8'))):
                    held_by = form.cleaned_data['held_by']
                    b = Book.from_gr_csv_dict(row, held_by)
                    print(b)
                    b.save()
            else:
                raise IOError("file too big")
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
