from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredients = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=110)
    categoria = models.CharField(max_length=110)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)