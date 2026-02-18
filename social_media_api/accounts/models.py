from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Requirement: following field as ManyToMany to self
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)