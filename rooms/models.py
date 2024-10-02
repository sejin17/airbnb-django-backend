from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):

    """ Room model definition """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room","Private Room")
        SHARED_ROOM = ("shared_room","Shared Room")


    name = models.CharField(max_length=150, default="")
    country = models.CharField(max_length=50, default="Australia")
    city= models.CharField(max_length=80, default="Sydney")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField (default= False)
    type = models.CharField(max_length=20, choices=RoomKindChoices.choices,)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    # many to many
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        )
    
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rooms",
    )
    def __str__(self) -> str:
        return self.name
    
    def total_amenities(self) -> int:
        return self.amenities.count()
    
    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class Amenity(CommonModel):

    """ Amenity Definition """

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length = 150,
        null=True,
        blank=True
    )

    def __str__(self)->str:
        return self.name
    
    class Meta:
        verbose_name_plural = "amenities"
    
