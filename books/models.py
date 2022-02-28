from django.db import models

# Create your models here.:
class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=150)
    number_of_pages = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title