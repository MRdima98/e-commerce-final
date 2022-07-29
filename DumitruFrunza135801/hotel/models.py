from unicodedata import decimal
from django.db import models

class Hotel(models.Model):
    name        = models.TextField()
    IVA         = models.TextField()
    street      = models.TextField()
    stars       = models.DecimalField(max_digits=1, decimal_places=0)
    cost        = models.DecimalField(max_digits=6, decimal_places=2)
    rooms       = models.DecimalField(max_digits=3, decimal_places=0)
    free_time   = models.TextField()
    CAP         = models.DecimalField(max_digits=5, decimal_places=0)
    city        = models.TextField()
    description = models.TextField()

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.TextField()
    start_period = models.DateField()
    stop_period = models.DateField()
    start_period2 = models.DateField()
    stop_period2 = models.DateField()
    start_period3 = models.DateField()
    stop_period3 = models.DateField()
    cost = models.DecimalField(max_digits= 6, decimal_places= 2)
    
    