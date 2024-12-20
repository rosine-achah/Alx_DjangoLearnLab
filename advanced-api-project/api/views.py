from rest_framework import serializers
from rest_framework.filters import SearchFilter, OrderingFilter

# from django_filters import rest_framework
from rest_framework import django_filters
import django_filters
from django_filters import rest_framework as filters

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import filters
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# from django_filters import rest_framework as filters
from rest_framework.filters import django_filters

# from rest_framework import BookFilter, DjangoFilterBackend

# Create your views here.


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    author = filters.CharFilter(lookup_expr="icontains")
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


# List view for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ["publication_year"]
    # ordering = ["publication_year"]
    filter_backends = (filter.DjangoFilterBackend, filters.SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]


# Detail view for retrieving a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create view for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Update view for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


# Delete view for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


# # ListView for all books
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# # class BookDetailView
# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "pk"


# # CreateView for adding a new book
# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def perform_create(self, serializer):

#         user = self.request.user
#         serializer.save(user=user)
#         return super().perform_create(serializer)


# # UpdateView for modifying an exisitng book
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# # DeleteView for removing a book
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
