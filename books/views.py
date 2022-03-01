from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from .forms import BookForm, BookFormSet

# Create your views here.
def create_book(request, pk):
    author = models.Author.objects.get(pk = pk)
    form = BookForm(request.POST or None)
    books = models.Book.objects.filter(author=author)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("book_details", pk=book.id)
        else:
            return render(request, "partials/add_form.html", {"form":form})

    context = {
        "author":author,
        "form":form,
        "books":books
    }
    return render(request, "create_book.html",context)

def create_book_htmx(request):
    context = {
        "form":BookForm(),
    }
    return render(request, "partials/add_form.html",context)

def book_update(request, pk):
    book = models.Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            book = form.save()
            return redirect("book_details", pk=book.id)
    context = {
        "form":form,
        "book":book
    }
    return render(request, "partials/add_form.html",context)

def book_details(request, pk):
    book = models.Book.objects.get(pk=pk)
    context= {
        "book":book
    }
    return render(request, "partials/book_details.html", context)

def book_delete(request, pk):
    book = models.Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')