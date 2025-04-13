from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Falta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_falta = models.DateField()
    respondida = models.BooleanField(default=False)  # Campo para indicar se a falta foi respondida

    def __str__(self):
        return f"Falta de {self.aluno.nome} em {self.data_falta} - {'Respondida' if self.respondida else 'Não Respondida'}"
