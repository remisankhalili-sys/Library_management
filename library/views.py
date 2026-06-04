# library/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Book, Author
from .forms import BookForm, AuthorForm


class BookListView(ListView):
    """
    View to display a list of all books.
    """
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 10  # Display 10 books per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        return context


class BookDetailView(DetailView):
    """
    View to display a specific book.
    """
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookCreateView(SuccessMessageMixin, CreateView):
    """
    View to create a new book.
    """
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')
    success_message = "Book '%(title)s' was created successfully."

    def form_valid(self, form):
        # Additional logic before saving (if needed).
        return super().form_valid(form)


class BookUpdateView(SuccessMessageMixin, UpdateView):
    """
    View to edit information about an existing book.
    """
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')
    success_message = "Book '%(title)s' was updated successfully."


class AuthorCreateView(SuccessMessageMixin, CreateView):
    """
    View to add a new author.
    """
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_add.html'
    success_url = reverse_lazy('author_add')
    success_message = "Author '%(first_name)s' was added successfully."

    def form_valid(self, form):
        # Simple validation: First and last name are required.
        if not form.cleaned_data.get('first_name') or not form.cleaned_data.get('last_name'):
            form.add_error('first_name', "First name is required.")
            return self.form_invalid(form)
    

        if not form.cleaned_data.get('last_name'):
            form.add_error('last_name', "Last name is required.")
            return self.form_invalid(form)
            
        return super().form_valid(form)