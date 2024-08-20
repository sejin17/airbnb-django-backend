from django.db import models

# Create your models here.
# we do not want this model to be in DB just want it to be referened in other models 

class CommonModel(models.Model):

    """ Common Model Deminition """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # DO NOT put this model into DB
    class Meta:
        abstract = True