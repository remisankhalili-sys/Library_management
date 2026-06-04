from django.contrib import admin
from .models import Book, Author



# Author display settings in the admin panel.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'get_total_books')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birth_date',)

    # Display the get_total_books method in the admin panel .
    def get_total_books(self, obj):
        return obj.books.count()
    get_total_books.short_description = 'Total Books'

# Book display settings in the admin panel.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'created_at')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'isbn')
    date_hierarchy = 'published_date'

admin.site.register(Book, BookAdmin)
