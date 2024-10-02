from django.db import models
from common.models import CommonModel

# Create your models here.

class Experience(CommonModel):

    """Experience model definition"""

    name = models.CharField(max_length=150, default="")
    country = models.CharField(max_length=50, default="Australia")
    city= models.CharField(max_length=80, default="Sydney")
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="experiences",
    )
    perk = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    start = models.TimeField()
    end = models.TimeField()
    
    def __str__(self) -> str:
        return self.name

class Perk(CommonModel):

    """ What is included on an Experience """
    
    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name
