from django import forms
from widgets import PaperTextInput
from models import Book, Person

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