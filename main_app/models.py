from django.db import models

# Create your models here.
class Place(models.Model):
    user_name = models.TextField()
    title = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)