from django.db import models
from common.models import CommonModel

# Create your models here.

class Booking(CommonModel):

    """Booking Model Definition """
    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    type = models.CharField(
        max_length = 15, 
        choices= BookingKindChoices.choices,
        )
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)

    experience_date = models.DateTimeField(blank=True, null=True)
