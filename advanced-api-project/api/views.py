from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ---------- LIST & CREATE ----------
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles GET (list all books) and POST (create a new book).
    - GET /books/ -> list of all books
    - POST /books/ -> create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to read, but only authenticated users can create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# ---------- DETAIL (RETRIEVE, UPDATE, DELETE) ----------
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve), PUT/PATCH (update), DELETE (remove).
    - GET /books/<id>/ -> retrieve single book
    - PUT /books/<id>/ -> update book
    - PATCH /books/<id>/ -> partial update
    - DELETE /books/<id>/ -> delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to read, but only authenticated users can update/delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

