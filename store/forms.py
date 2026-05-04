# store/forms.py
from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = ['title', 'publish_date', 'publisher', 'price', 'category', 'store', 'author']


class AuthorForm(forms.ModelForm):
    class Meta:
        model  = Author
        fields = ['first_name', 'last_name']
