from django import forms
from django.core.exceptions import ValidationError

from .models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'dateline', 'genre', 'addition', 'rating']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'dateline': forms.TextInput(attrs={'class': 'form-control'}),
        'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'addition': forms.Textarea(attrs={'class': 'form-control'}),
        'rating': forms.SelectMultiple(attrs={'class': 'form-control'})
    }

    def clean_book(self):
        new_book = self.cleaned_data['book'].lower()

        if new_book == 'create':
            raise ValidationError('Book may be not create')
        return new_book
