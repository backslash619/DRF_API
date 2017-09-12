from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews')
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
