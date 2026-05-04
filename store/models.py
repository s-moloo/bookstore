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