from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # you can use this way.
    # title = serializers.CharField(max_length=150)

    class Meta:
        model = Book
        fields = ("id", "title", "content", "subtitle", "author", "isbn", "price")

    def validate(self, data):
        title = data.get("title", None)
        isbn = data.get("isbn", None)

        # Checking the title is not only a number!
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "books": "title must be str!",
                }
            )

        # Checking isbn is not the same as others.
        if Book.objects.filter(title=title, isbn=isbn).exists():
            raise ValidationError(
                {
                    "status": False,
                    "books": "The title and ISBN must be Unique!",
                }
            )
        return data

    # def validate_price(self, price):
    #     if price < 0 or price > 9999999999:
    #         raise ValidationError(
    #             {
    #                 "status": False,
    #                 "message": "Wrong value of price!",
    #             }
    #         )
