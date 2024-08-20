from django.db import models
from common.models import CommonModel
# Create your models here.

# Create photo model
class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
        null=True, 
        blank=True
        )
    room= models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return "Photo File"

# Create video model
class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return "Video file"