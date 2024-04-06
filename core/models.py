from django.db import models
from users.models import User

class Post(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    comments = models.TextField(max_length=300, null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    liked_by = models.ManyToManyField(User, related_name='liked_posts')
    disliked_by = models.ManyToManyField(User, related_name='disliked_posts')
