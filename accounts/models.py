from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from core.mixins import TimeStampedMixin
class User(AbstractUser, TimeStampedMixin):

    email = models.EmailField(
        "Email Address",
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    objects = UserManager()

    class Meta:
        ordering = ["username"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name() or self.username
        
        
        