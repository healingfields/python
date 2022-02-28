from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.
class BookInlineAdmin(admin.TabularInline):
    model = models.Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]

admin.site.register(models.Author, AuthorAdmin)
