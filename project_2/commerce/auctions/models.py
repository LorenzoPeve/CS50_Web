from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = [
    "Electronics", "Fashion", "Home & Furniture", "Health & Beauty",
    "Sports & Outdoors", "Toys & Games", "Books & Media", "Automotive",
    'Collectibles & Art'
]

class User(AbstractUser):
    pass

class Listing(models.Model):

    cats = [(c,c) for c in CATEGORIES]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255)
    current_bid =  models.FloatField()
    image_url = models.URLField(default=r"https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/image-not-available.jpg")
    category = models.CharField(max_length=20, choices=cats)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'listing')