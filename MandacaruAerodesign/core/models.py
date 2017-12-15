from django.db import models

# Create your models here.
class infoPS(models.Model):
    ativo = models.BooleanField(default=False)