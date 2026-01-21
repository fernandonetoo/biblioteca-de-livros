from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    
    def __str__(self):
        return self.titulo