from django import forms
from widgets import PaperTextInput
from models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {
            'title': PaperTextInput
        }