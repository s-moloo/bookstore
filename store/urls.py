from django.urls import path
from . import views

urlpatterns = [
    # Stores
    path('',                 views.StoreListView.as_view(),  name='store-list'),
    path('store/<int:pk>/', views.StoreDetailView.as_view(), name='store-detail'),

    # Books
    path('books/',                    views.BookListView.as_view(),       name='book-list'),
    path('books/add/',                views.BookCreateView.as_view(),     name='book-create'),
    path('books/<int:pk>/edit/',      views.BookUpdateView.as_view(),     name='book-update'),
    path('books/<int:pk>/delete/',    views.BookDeleteView.as_view(),     name='book-delete'),
    path('books/<int:pk>/inline-delete/',
                                     views.BookInlineDeleteView.as_view(),
                                     name='book-inline-delete'),
    # HTMX search endpoint
    path('books/search/',             views.BookSearchView.as_view(),     name='book-search'),

    # Authors
    path('authors/',                 views.AuthorListView.as_view(),    name='author-list'),
    path('authors/<int:pk>/',        views.AuthorDetailView.as_view(),  name='author-detail'),
    path('authors/add/',             views.AuthorCreateView.as_view(),  name='author-create'),
    path('authors/<int:pk>/edit/',   views.AuthorUpdateView.as_view(),  name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(),  name='author-delete'),
]