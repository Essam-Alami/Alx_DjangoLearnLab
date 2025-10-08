from django.db import models
from django.contrib.auth.models import AbstractUser

def profile_image_upload_to(instance, filename):
    return f'profiles/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=profile_image_upload_to, null=True, blank=True)
    # followers: users who follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def follower_count(self):
        return self.followers.count()

    def __str__(self):
        return self.username
    
    
