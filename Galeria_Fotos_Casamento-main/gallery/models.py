from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    nome = models.CharField(max_length=255)
    capa = models.ImageField(upload_to='capas_albuns/')

    def __str__(self):
        return self.nome

class Foto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='fotos/')
    descricao = models.TextField(blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)
    enviado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Foto de {self.enviado_por} no álbum {self.album}"

class Curtida(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='curtidas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentario(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
