from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
    BookCreateAPIView,
    BookListCreateAPIView,
    BookUpdateDeleteAPIView,
    BookViewSet,
)

router = SimpleRouter()
router.register("books", BookViewSet, basename="books")

urlpatterns = [
    # path("books/", BookListAPIView.as_view()),
    # path("books/<int:pk>/", BookDetailAPIView.as_view()),
    # path("books/create/", BookCreateAPIView.as_view()),
    # path("book/", BookListCreateAPIView.as_view()),
    # path("books/<int:pk>/delete/", BookDeleteAPIView.as_view()),
    # path("books/<int:pk>/update/", BookUpdateAPIView.as_view()),
    # path("books/<int:pk>/update-delete/", BookUpdateDeleteAPIView.as_view()),
]

urlpatterns += router.urls
