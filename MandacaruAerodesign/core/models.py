from django.db import models

# Create your models here.
class infoPS(models.Model):
    ativo = models.BooleanField(default=False)

class member(models.Model):
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    # foto = models.FileField()
    foto = models.ImageField(upload_to="membros/")

    def __str__(self):
        return self.nome

class patroc(models.Model):
    # foto = models.FileField()
    foto = models.ImageField(upload_to="patrocinadores/")
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao