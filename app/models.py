from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Place(models.Model):
    user_name = models.TextField()
    title = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)