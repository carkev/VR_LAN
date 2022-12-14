from django.urls import reverse
from django.db import models


# Create your models here.

class Function(models.Model):
    """...
    """
    function = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.function


    def get_absolute_url(self):
        return reverse("function_detail",args={str(self.pk)})

    class Meta:
        db_table="function"


class Staff(models.Model):
    """ Modèle des membres de VRLan.
    """
    firstname = models.CharField(verbose_name="Prénom",max_length=30, null=False)
    lastname = models.CharField(verbose_name="Nom",max_length=40, null=False)
    email = models.EmailField(verbose_name="Email",null=True)
    function = models.ForeignKey(Function(),on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name="Photo")

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return reverse("staff_detail",args={str(self.pk)})

    class Meta:
        db_table="staff"


