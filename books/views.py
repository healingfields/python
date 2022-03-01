from django.shortcuts import redirect, render
from . import models
from .forms import BookForm, BookFormSet

# Create your views here.
def create_book(request, pk):
    author = models.Author.objects.get(pk = pk)
    formset = BookFormSet(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create_book", pk=author.id)
    context = {
        "author":author,
        "formset":formset
    }
    return render(request, "create_book.html",context)

def create_book_htmx(request):
    context = {
        "form":BookForm()
    }
    return render(request, "partials/add_form.html",context)