from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = "tinylibrary"

urlpatterns = [
    url(r"^(?P<pk>\d+)/$", views.DetailBook.as_view(), name="book-detail"),
    url(r"^new/$", views.CreateBook.as_view(), name="book-new"),
    url(r"^$", views.IndexView.as_view(), name="book-home"),
    url(r"^(?P<pk>\d+)/update/$", views.UpdateBook.as_view(), name="book-update"),
    url(r"^(?P<pk>\d+)/delete/$", views.DeleteBook.as_view(), name="book-delete"),
    url(r"^newPerson/$", views.CreatePerson.as_view(), name="person-create"),
    url(r"^quagga/$", views.QuaggaTest.as_view(), name="quagga-test"),
    url(r"^button/$", views.ButtonsTest.as_view(), name="button-test"),
    url(r"^fromISBN/$", views.CreateBookFromISBN.as_view(), name="from-isbn"),
    url(r"^import_csv/$", views.ImportCSV.as_view(), name="import-csv"),
    path("help", views.HelpView.as_view(), name="help"),
]
