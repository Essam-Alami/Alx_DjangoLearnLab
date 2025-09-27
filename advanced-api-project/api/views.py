from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters


# ---------- LIST ----------
class BookListView(generics.ListAPIView):
    """
    GET /books/ → Retrieve all books with filtering, searching, and ordering.
    - Filtering: ?author=<id>&publication_year=<year>
    - Searching: ?search=keyword (matches title or author name)
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields
    search_fields = ['title', 'author__name']  # double underscore to search related field

    # Orderable fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

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


