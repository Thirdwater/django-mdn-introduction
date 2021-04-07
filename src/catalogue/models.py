import uuid

from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text="E.g. Philosophy, Mathematics, Computer Science.")

    def __str__(self):
        """String representing the genre object."""
        return self.name


class Language(models.Model):
    """Model representing a book language."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String representing the language object."""
        return self.name


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String representing the author object."""
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        """URL to access a detail record for this author."""
        return reverse('author-detail', args=[self.id])


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    author = models.ManyToManyField(Author)

    description = models.TextField(max_length=10_000, blank=True, null=True,
        help_text="Brief description of this book.")

    ISBN_LINK = "https://www.isbn-international.org/content/what-isbn"
    isbn = models.CharField('ISBN', max_length=13, unique=True,
        help_text=f"13-digit <a href=\"{ISBN_LINK}\">ISBN number</a> for this book.")

    genre = models.ManyToManyField(Genre, help_text="Genre(s) for this book.")

    language = models.ManyToManyField(Language, help_text="Language(s) for this book.")

    def __str__(self):
        """String representing the book object."""
        return self.title

    def get_absolute_url(self):
        """URL to access a detail record for this book."""
        return reverse('book-detail', args=[self.id])


class BookCopy(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        help_text="A unique ID for this copy across the whole library.")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)

    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)

    class LOAN_STATUS:
        MAINTENANCE = 'm'
        ON_LOAN = 'o'
        AVAILABLE = 'a'
        RESERVED = 'r'
    LOAN_STATUS_CHOICES = [
        (LOAN_STATUS.MAINTENANCE, 'Maintenance'),
        (LOAN_STATUS.ON_LOAN, 'On loan'),
        (LOAN_STATUS.AVAILABLE, 'Available'),
        (LOAN_STATUS.RESERVED, 'Reserved'),
    ]
    loan_status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS_CHOICES,
        blank=True,
        default=LOAN_STATUS.MAINTENANCE,
        help_text="Current availability for this book copy.",
    )

    class Meta:
        ordering = ['due_date']
        verbose_name_plural = "Book copies"

    def __str__(self):
        """String representing the book copy object."""
        return f"{self.id} ({self.book.title})"
