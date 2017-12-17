from django.db import models

# Create your models here.
class infoPS(models.Model):
    ativo = models.BooleanField(default=False)

class member(models.Model):
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    foto = models.FileField()

class patroc(models.Model):
    foto = models.FileField()
    descricao = models.CharField(max_length=100)