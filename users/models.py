from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    friends = models.ManyToManyField('self', symmetrical=False, blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='request_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='request_received', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    