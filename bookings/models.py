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
        related_name="bookings",
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings"
    )
    check_in = models.DateField(
        blank=True, 
        null=True,
        )
    check_out = models.DateField(
        blank=True, 
        null=True,
        )

    experience_date = models.DateTimeField(
        blank=True, 
        null=True,
        )
    
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"
