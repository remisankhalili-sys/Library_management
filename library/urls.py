# library/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/add/', views.BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author_add'),
]