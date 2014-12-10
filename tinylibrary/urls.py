from django.conf.urls import patterns, url
from views import index, book, CreateBook
urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', book.as_view(), name="book-detail"),
                       url(r'^new/$', CreateBook.as_view()),
                       url(r'^$', index.as_view()),


                       )
