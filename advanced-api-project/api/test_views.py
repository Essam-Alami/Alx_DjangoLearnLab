from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book
from django.contrib.auth.models import User


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication (if your API requires it)
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Sample books
        self.book1 = Book.objects.create(title="Django Unleashed", author="Andrew Pinkham", publication_year=2015)
        self.book2 = Book.objects.create(title="Two Scoops of Django", author="Daniel Roy", publication_year=2019)
        self.book3 = Book.objects.create(title="Learning Python", author="Mark Lutz", publication_year=2013)

        # Endpoints
        self.list_url = reverse("book-list")  # check your urls.py naming
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])

    def test_create_book(self):
        data = {"title": "New Book", "author": "John Doe", "publication_year": 2020}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_update_book(self):
        data = {"title": "Updated Django", "author": "Andrew Pinkham", "publication_year": 2016}
        response = self.client.put(self.detail_url(self.book1.id), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # --- Filtering, Searching, Ordering ---
    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=Mark Lutz")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Mark Lutz")

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
