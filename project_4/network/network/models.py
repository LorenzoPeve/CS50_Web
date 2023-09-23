from django.contrib.auth.models import AbstractUser
from django.db import models


from datetime import datetime, timezone, timedelta
EST = timezone(timedelta(hours=-5)) # US Eastern Time UTC-5

class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post
    content = models.TextField()
    created_at = models.DateTimeField(datetime.now(EST))
    updated_at = models.DateTimeField(default=datetime.now(EST))

    def total_likes(self):
        return Like.objects.filter(post=self).count()

class Following(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follows = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} follows {self.follows.username}"
    
    class Meta:
        unique_together = ['user', 'follows']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Author of the post

    class Meta:
        unique_together = ['user', 'post']