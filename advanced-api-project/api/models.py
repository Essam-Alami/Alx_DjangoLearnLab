from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents a writer with a unique name.
    One Author can have multiple Books (One-to-Many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Stores the title and publication year of a book.
    Each book is linked to a single Author (ForeignKey).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name="books",  # allows reverse access: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"