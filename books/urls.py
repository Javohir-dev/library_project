from django.urls import path

from .views import (
    book_list_view,
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
)

urlpatterns = [
    path("", BookListAPIView.as_view()),
    path("<int:pk>/", BookDetailAPIView.as_view()),
    path("<int:pk>/delete/", BookDeleteAPIView.as_view()),
    path("<int:pk>/update/", BookUpdateAPIView.as_view()),
    path("books/", book_list_view),
]
