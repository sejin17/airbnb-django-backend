from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    """ room or experience category """

    class CategoryKindChoices(models.TextChoices):
        ROOM = "rooms", "Rooms"
        EXPERIENCE = "experiences", "Experiences"

    name = models.CharField(max_length=150, blank=True)
    type = models.CharField(max_length=150, blank=True, choices=CategoryKindChoices.choices)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"