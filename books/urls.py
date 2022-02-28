from django.urls import path
from .views import create_book

urlpatterns = [
    path("create_book/<pk>", create_book, name="create_book")
]