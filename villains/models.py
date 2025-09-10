from django.db import models

# Create your models here.

class Villain(models.Model):
    codinome = models.CharField(max_length=50)
    nome_real = models.CharField(max_length=50, null=True)
    poderes = models.TextField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    historia = models.TextField(null=True)
    criado_em = models.DateTimeField(auto_now=True)