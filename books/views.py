from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    get_object_or_404,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

#! first way
# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


#! second way
class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data,
        }

        return Response(data)


# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": "Successfull",
                "book": serializer_data,
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": "Error!",
                    "message": "This book was not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# class BookDeleteAPIView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    "status": "True.",
                    "message": "Successfull deleted.",
                },
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                {
                    "status": "Error!",
                    "message": "This book was not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


# class BookUpdateAPIView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        books = Book.objects.all()
        book = get_object_or_404(books, id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "message": f"Book `{book_saved}` updated Successfully.",
            },
            status=status.HTTP_200_OK,
        )


# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"status": "Books created", "books": data}

        return Response(data, status=status.HTTP_200_OK)


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# @api_view(["GET"])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)

#     return Response(serializer.data)
