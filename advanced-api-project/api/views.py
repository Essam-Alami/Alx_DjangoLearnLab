from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# ---------- LIST ----------
class BookListView(generics.ListAPIView):
    """
    GET /books/ → Retrieve all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------- DETAIL ----------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/ → Retrieve a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------- CREATE ----------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/ → Add a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ---------- UPDATE ----------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/ → Update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ---------- DELETE ----------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/ → Remove a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


