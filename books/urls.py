from unicodedata import name
from django.urls import path
from .views import book_delete, book_details, create_book, create_book_htmx

urlpatterns = [
    path("create_book/<pk>", create_book, name="create_book"),
    path("create_book_htmx", create_book_htmx, name="create_book_htmx"),
    path('book_details/<pk>', book_details, name="book_details"),
    path("delete_book/<pk>", book_delete, name="book_delete")

] 