from django.conf.urls import url
import views

urlpatterns = [
               url(r'^(?P<pk>\d+)/$', views.book.as_view(), name="book-detail"),
               url(r'^new/$', views.CreateBook.as_view(), name="book-new"),
               url(r'^$', views.index.as_view(), name="book-home"),
               url(r'^(?P<pk>\d+)/update/$', views.UpdateBook.as_view(), name="book-update"),
               url(r'^(?P<pk>\d+)/delete/$', views.DeleteBook.as_view(), name="book-delete"),
               url(r'^newPerson/$', views.CreatePerson.as_view(), name="person-create"),
               url(r'^quagga/$', views.QuaggaTest.as_view(), name='quagga-test'),
               url(r'^fromISBN/$', views.CreateBookFromISBN.as_view(), name='from-isbn'),
               url(r'^import_csv/$', views.ImportCSV.as_view(), name='import-csv'),
]
