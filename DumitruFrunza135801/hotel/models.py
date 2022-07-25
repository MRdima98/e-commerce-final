from unicodedata import decimal
from django.db import models

class Hotel(models.Model):
    name      = models.TextField()
    IVA       = models.TextField()
    street    = models.TextField()
    stars     = models.DecimalField(max_digits=1, decimal_places=0)
    cost      = models.DecimalField(max_digits=1000000, decimal_places=2)
    rooms     = models.DecimalField(max_digits=1000, decimal_places=0)
    free_time = models.TextField()
    CAP       = models.DecimalField(max_digits=5, decimal_places=0)
    city      = models.TextField()

    