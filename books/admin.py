from django.contrib import admin
from .models import Book


@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "author", "price"]
    list_filter = ["author", "price"]
    search_fields = ["title", "author"]
    ordering = ["price"]
