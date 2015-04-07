from django import forms
from django.forms.models import modelform_factory
from widgets import PaperTextInput
from models import Book, Person



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
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
        fields = '__all__'
        labels={'name':'',}
        widgets={'name': PaperTextInput,}

