from unicodedata import decimal
from django.db import models

class Hotel(models.Model):
    name = models.TextField()
    IVA = models.TextField()
    street = models.TextField()
    stars = models.IntegerField()
    cost = models.IntegerField()
    rooms = models.IntegerField()