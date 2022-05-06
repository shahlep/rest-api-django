from django.db import models


class Library(models.Model):
    book_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=5)
    aisle = models.IntegerField(max_length=4)
