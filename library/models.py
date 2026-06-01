from django.db import models

from django.urls import reverse


class Author(models.Model):
    """
    Represents an author in the library system.
    
    This model stores personal information about authors, including their
    first name, last name, biography, and date of birth. It also provides
    a method to count the total number of books written by the author.
    
    Attributes:
        first_name (str): The author's first name (max 100 characters).
        last_name (str): The author's last name (max 100 characters).
        bio (str): A brief biography or description of the author.
        birth_date (date): The author's date of birth.
    """
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Date of Birth")

    class Meta:
        """
        Options for the Author model.
        
        - ordering: Sorts authors by last name, then first name.
        - verbose_name/plural: Human-readable names for the admin interface.
        """
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """
        Returns the full name of the author as a string.
        
        Returns:
            str: The author's full name.
        """
        return f"{self.first_name} {self.last_name}"

    def get_total_books(self):
        """
        Calculates and returns the total number of books written by this author.
        
        This method utilizes the reverse relation defined in the Book model
        (related_name='books') to count associated book records.
        
        Returns:
            int: The count of books associated with this author.
        """
        return self.books.count()


class Book(models.Model):
    """
    Represents a book in the library system.
    
    This model stores details about books, including the title, author,
    publication date, and ISBN. It automatically tracks when the book
    was created and last updated.
    
    Attributes:
        title (str): The title of the book (max 200 characters).
        author (ForeignKey): The author who wrote the book.
        published_date (date): The date the book was published.
        isbn (str): The unique ISBN identifier for the book (max 13 characters).
        created_at (datetime): The timestamp when the record was created.
        updated_at (datetime): The timestamp when the record was last modified.
    """
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        verbose_name="Author"
    )
    published_date = models.DateField(null=True, blank=True, verbose_name="Publication Date")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        """
        Options for the Book model.
        
        - ordering: Sorts books by publication date (newest first).
        - verbose_name/plural: Human-readable names for the admin interface.
        """
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-published_date']

    def __str__(self):
        """
        Returns the title of the book as a string.
        
        Returns:
            str: The book's title.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the absolute URL to the detail view of this book.
        
        This is useful for generating links in templates and the admin interface.
        
        Returns:
            str: The URL path for the book's detail page.
        """
        return reverse('book_detail', kwargs={'pk': self.pk})