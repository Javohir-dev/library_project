from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
