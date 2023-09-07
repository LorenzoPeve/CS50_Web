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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255)
    current_bid =  models.FloatField()
    image_url = models.URLField(default=r"https://portfolio8aff35a6cba45be.blob.core.windows.net/djangoapp/image-not-available.jpg")
    category = models.CharField(max_length=20, choices=cats)
    status = models.CharField(
        max_length=20,
        choices=[('closed', 'closed'), ('active', 'active')],
        default='active')

    def __str__(self):
        return f"Listing {self.id}: {self.title}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"Comment on Listing {self.listing.id} by {self.author.username} at {self.date}"


class Watchlist(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'listing')


class Bids(models.Model):
    pass