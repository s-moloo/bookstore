from django.core.management.base import BaseCommand
from store.models import Store, Author, Book
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 4 stores
        b1 = Store.objects.create(
            name='North',
            city='Calgary',
            opened_date=datetime.date(2010, 3, 15),
        )
        b2 = Store.objects.create(
            name='South',
            city='Calgary',
            opened_date=datetime.date(2015, 7, 1),
        )
        b3 = Store.objects.create(
            name='Central',
            city='Mississauga',
            opened_date=datetime.date(2018, 1, 20),
        )
        b4 = Store.objects.create(
            name='East',
            city='Scarborough',
            opened_date=datetime.date(2021, 9, 5),
        )

        # 3 sellers — some work at multiple branches
        s1 = Author.objects.create(first_name='F. Scott', last_name='Fitzgerald')
        s2 = Author.objects.create(first_name='Harper', last_name='Lee')
        s3 = Author.objects.create(first_name='George', last_name='O')

        s1.stores.set([b1, b2])   # Alice works at two branches
        s2.stores.set([b1, b3])
        s3.stores.set([b2, b3, b4])

        # a few books
        Book.objects.create(title='The Great Gatsby', publish_date=datetime.date(1925, 4, 10),
                            publisher='Scribner', price=12.99, category='FIC',
                            store=b1, author=s1)
        Book.objects.create(title='To Kill a Mockingbird', publish_date=datetime.date(1960, 7, 11),
                            publisher='J.B. Lippincott & Co.', price=15.99, category='FIC',
                            store=b1, author=s2)
        Book.objects.create(title='1984', publish_date=datetime.date(1948, 6, 8),
                            publisher='Secker & Warburg', price=13.99, category='FIC',
                            store=b2, author=s3,)
        Book.objects.create(title='The Catcher in the Rye', publish_date=datetime.date(1951, 7, 16),
                            publisher='Little, Brown and Company', price=14.99, category='FIC',
                            store=b3, author=s2)
        Book.objects.create(title='The Hobbit', publish_date=datetime.date(1937, 9, 21),
                            publisher='George Allen & Unwin', price=16.99, category='FIC',
                            store=b3, author=s2)

        self.stdout.write(self.style.SUCCESS('Database seeded!'))