# accounts/models.py
"""Custom user model."""
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """User customized model.

    :parent: AbstractUser
    """
    pass
