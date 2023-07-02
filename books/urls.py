from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
    BookCreateAPIView,
    BookListCreateAPIView,
    BookUpdateDeleteAPIView,
)

urlpatterns = [
    path("books/", BookListAPIView.as_view()),
    path("books/<int:pk>/", BookDetailAPIView.as_view()),
    path("book-list-create/", BookCreateAPIView.as_view()),
    path("book/", BookListCreateAPIView.as_view()),
    path("books/<int:pk>/delete/", BookDeleteAPIView.as_view()),
    path("books/<int:pk>/update/", BookUpdateAPIView.as_view()),
    path("books/<int:pk>/update-delete/", BookUpdateDeleteAPIView.as_view()),
]
