from django.db import models
from user.models import Heroi
from blog.models import Post

# Create your models here.

class Comentario(models.Model):
    texto = models.TextField(null=True)
    data_de_postagem = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Heroi, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
