from django.conf import settings
from django.db import models


class Truck(models.Model):
    "Generated Model"
    color = models.CharField(
        max_length=256,
    )
    model = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    count_tires = models.IntegerField(
        null=True,
        blank=True,
    )


# Create your models here.
