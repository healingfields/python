from django import forms 
from django.forms.models import inlineformset_factory
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            "title",
            "number_of_pages"
        )


BookFormSet = inlineformset_factory(
    models.Author,
    models.Book,
    BookForm,
    can_delete=False,
    min_num=3,
    extra=0
)