# Django + HTMX
## CRUD Operations & Search with Class-Based Views
### Book Store

# models.py

from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    opened_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.city}'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    stores = models.ManyToManyField(
        Store,
        related_name='authors',
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):   # ✅ now at top level
    CATEGORY_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science'),
        ('HIS', 'History'),
    ]

    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    publisher = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default='FIC'
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='books',
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books',
    )

    def __str__(self):
            return f'{self.title} by {self.author.first_name} {self.author.last_name} - {self.get_category_display()}'


# views.py

# store/views.py
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from .models import Store, Author, Book
from .forms  import BookForm, AuthorForm


# ── Stores ───────────────────────────────────────────────────────────────

class StoreListView(ListView):
    model               = Store
    template_name       = 'store/store_list.html'
    context_object_name = 'stores'


class StoreDetailView(DetailView):
    model               = Store
    template_name       = 'store/store_detail.html'
    context_object_name = 'store'

    # 🔑 KEY CONCEPT: add extra context from related models
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # store.books uses the related_name we set on Book.store
        ctx['books']    = self.object.books.select_related('author')
        # store.authors uses the ManyToManyField related_name
        ctx['authors'] = self.object.authors.filter(is_active=True)
        return ctx


# ── Books ───────────────────────────────────────────────────────────────────

class BookListView(ListView):
    model               = Book
    template_name       = 'store/book_list.html'
    context_object_name = 'books'
    # Eager-load author to avoid N+1 queries
    queryset            = Book.objects.select_related('author')


class BookCreateView(CreateView):
    model         = Book
    form_class    = BookForm
    template_name = 'store/book_form.html'
    success_url   = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model         = Book
    form_class    = BookForm
    template_name = 'store/book_form.html'
    success_url   = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model         = Book
    template_name = 'store/book_confirm_delete.html'
    success_url   = reverse_lazy('book-list')


# ── HTMX: live search (returns a partial HTML fragment) ────────────────────

class BookSearchView(ListView):
    model               = Book
    # Returns a partial template, not a full page
    template_name       = 'store/partials/book_table.html'
    context_object_name = 'books'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = Book.objects.select_related('author')
        if q:
            qs = qs.filter(
                Q(title__icontains=q)  |
                Q(author__name__icontains=q)
            )
        return qs
    
    # ── Authors ────────────────────────────────────────────────────────────────

class AuthorListView(ListView):
    model               = Author
    template_name       = 'store/author_list.html'
    context_object_name = 'authors'
    queryset            = Author.objects.prefetch_related('books')


class AuthorDetailView(DetailView):
    model               = Author
    template_name       = 'store/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['books'] = self.object.books.select_related('store')
        return ctx


class AuthorCreateView(CreateView):
    model         = Author
    form_class    = AuthorForm
    template_name = 'store/author_form.html'
    success_url   = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model         = Author
    form_class    = AuthorForm
    template_name = 'store/author_form.html'
    success_url   = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model         = Author
    template_name = 'store/author_confirm_delete.html'
    success_url   = reverse_lazy('author-list')


# ── HTMX: inline delete returns empty 200 so HTMX removes the row ──────────

class BookInlineDeleteView(DeleteView):
    model = Book

    def form_valid(self, form):
        self.object.delete()
        # Return empty response — HTMX replaces the deleted row with nothing
        return HttpResponse('')

---


<img width="477" height="223" alt="image" src="https://github.com/user-attachments/assets/2a258b91-3b71-4450-8d83-866a2b25004c" />

<img width="501" height="456" alt="image" src="https://github.com/user-attachments/assets/720c9530-eecf-48f4-8ead-aea400d41f02" />

<img width="533" height="434" alt="image" src="https://github.com/user-attachments/assets/721a76ae-2a6d-43a0-afd9-85efaf0e433b" />

<img width="456" height="421" alt="image" src="https://github.com/user-attachments/assets/faad1899-fce7-431f-b65a-bd91870ccdf0" />

<img width="340" height="417" alt="image" src="https://github.com/user-attachments/assets/763f4998-7a11-4b81-811a-23c522391e35" />





