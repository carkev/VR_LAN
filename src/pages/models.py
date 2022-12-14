"""...
"""
from django.db import models


# Create your models here.
class StaffRole(models.Model):
    """...
    """
    name = models.CharField(max_length=50)


class Staff(models.Model):
    """...
    """
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    mail = models.EmailField()
    picture = models.ImageField(upload_to='staff_pictures', blank=True)
    staff_role = models.ForeignKey(StaffRole, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
