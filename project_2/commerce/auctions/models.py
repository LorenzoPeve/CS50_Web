from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = [
    "Electronics", "Fashion", "Home and Furniture", "Health and Beauty",
    "Sports and Outdoors", "Toys and Games", "Books and Media", "Automotive"
]

class User(AbstractUser):
    pass

class Listing(models.Model):

    cats = [(c,c) for c in CATEGORIES]
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255)
    current_bid =  models.FloatField()
    image_url = models.URLField(default=r"https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/image-not-available.jpg")
    category = models.CharField(max_length=20, choices=cats)
# class Bid(models.Model):
#     pass

# class Comment(models.Model):
#     pass


# class MyModel(models.Model):
#     my_charfield = models.CharField(max_length=32, blank=False)

# MyModel().save()