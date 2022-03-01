from django.urls import path
from .views import create_book, create_book_htmx

urlpatterns = [
    path("create_book/<pk>", create_book, name="create_book"),
    path("create_book_htmx", create_book_htmx, name="create_book_htmx")

] 