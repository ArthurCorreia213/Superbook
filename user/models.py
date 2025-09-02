from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Heroi(AbstractUser):
    email = models.EmailField()
    poderes = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)

    REQUIRED_FIELDS=['email', 'poderes', 'estado', 'cidade', 'password1', 'password2']