from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # you can use this way.
    # title = serializers.CharField(max_length=150)

    class Meta:
        model = Book
        fields = ("id", "title", "content", "subtitle", "author", "isbn", "price")
