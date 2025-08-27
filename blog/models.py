from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(null=True)
    imagem = models.ImageField(null=True)
    data_de_postagem = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('posts')