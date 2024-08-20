from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # customize fieldsets to match the custom user model
    # fieldsets = None
    # fields = ("email","password","name")

    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "profile_photo",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency"
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            }
        )
    )