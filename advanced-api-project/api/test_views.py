from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
# from rest_framework import django_filters


class BookAPITests(APITestCase):

    def setUp(self):
        # create a test user for authentication
        self.user = User.objects.create_user(
            username="test_user", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        self.author = Author.objects.create(name="J.K Rowling")
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of secrets",
            publication_year=1998,
            author=self.author,
            
        )

    def test_create_book(self):
        url = "/books/"
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1990,
            "author": self.author.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_books(self):
        url = "/books/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        url = f"/books/{self.book1.id}/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["title"], "Harry Potter and the Sorcerer's Stone"
        )

    def test_update_book(self):
        url = f"/books/{self.book1.id}/"
        data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 1997,
            "author": self.author.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()  # Refresh the instance from the DB
        self.assertEqual(self.book1.title, "Harry Potter and the Philosopher's Stone")

    def test_delete_book(self):
        url = f"/books/{self.book1.id}/"
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only one book should remain

    def test_filter_books_by_title(self):
        url = "/books/?title=Chamber"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book should match

    def test_search_books(self):
        url = "/books/?search=Rowling"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), 2
        )  # Both books by J.K. Rowling should match

    def test_order_books_by_publication_year(self):
        url = "/books/?ordering=publication_year"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["title"], "Harry Potter and the Sorcerer's Stone"
        )
