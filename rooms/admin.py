from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "type",
        "owner",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "type",
        "amenities",
        "created_at",
        "updated_at",
    )

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )