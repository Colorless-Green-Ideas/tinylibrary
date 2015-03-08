from django import forms
from widgets import PaperTextInput
from models import Book

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