from django.test import TestCase
from django.forms.models import modelform_factory

from materialdjango.forms import mangle_form

from .models import Book

class FormMangleTest(TestCase):
    def test_mangle_form(self):
        fact = modelform_factory(Book,fields="__all__")
        x = mangle_form(fact())
        print x
