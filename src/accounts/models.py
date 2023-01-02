# accounts/models.py
"""Custom user model."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    """User customized model.

    :parent: AbstractUser
    """
    def get_absolute_url(self):
        return reverse('users_profile',args=[str(self.pk)])



