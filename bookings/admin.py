from django.contrib import admin
from .models import Booking
# Register your models here.
@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = (
        "type",
        "user",
        "room",
        "experience",
        "check_in",
        "check_out",
        "experience_date",
        "guests",
    )