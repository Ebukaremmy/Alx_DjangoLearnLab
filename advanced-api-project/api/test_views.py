from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='password123')
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        self.client.login(username='tester', password='password123')
        data = {"title": "New Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filter_books(self):
        response = self.client.get('/api/books/?title=Harry Potter')
        self.assertEqual(len(response.data), 1)