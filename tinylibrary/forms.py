from django import forms
from django.forms.models import modelform_factory
from widgets import PaperTextInput
from models import Book, Person

def mangle_form(form):
    "Utility to mangle forms into paperinputs, untested"
    for field in form.fields:
        if type(field.widget) is forms.widgets.Textarea:
            field.widget = PaperTextInput()
            field.label = ''
    return form

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        labels={'title': '',
                'isbn': '',
                'author': '',}
        widgets = {
            'title': PaperTextInput,
            'isbn' : PaperTextInput,
            'author': PaperTextInput,
        }
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        labels={'name':'',}
        widgets={'name': PaperTextInput,}

