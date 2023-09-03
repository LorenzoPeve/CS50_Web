from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=255)
    current_bid =  models.FloatField()
    image_url = models.URLField()

class Bid(models.Model):
    pass

class Comment(models.Model):
    pass