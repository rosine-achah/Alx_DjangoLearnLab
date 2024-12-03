from rest_framework import serializers
from .models import Book, Author
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model. It includes fields like 'title', 'publication_year', and a reference to 'author'.
    Custom validation ensures that the publication year is not in the future.
    """

    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. It includes the author's name and a nested list of their books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
        # fields = "__all__"


# Author and Book have a one to many relationship
