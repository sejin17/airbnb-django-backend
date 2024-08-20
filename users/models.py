from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
'''
class User(models.Model):
    pass

'''

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male","Male") #(DB value, admin panel value)
        FEMALE = ("female","Female")
        
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        KRW = ("krw", "Korean Won")
        USD = ("usd", "US Dollar")

    first_name = models.CharField(("first name"), max_length=150, blank=True, editable=False)
    last_name = models.CharField(("last name"), max_length=150, blank=True, editable=False)
    profile_photo = models.ImageField(blank=True)
    name = models.CharField(("name"), max_length=150, blank=True)
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=10, choices = LanguageChoices.choices,)
    currency = models.CharField(max_length=10, choices = CurrencyChoices.choices, )