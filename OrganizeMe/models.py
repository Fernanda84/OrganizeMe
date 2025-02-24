from django.db import models
from django.contrib.auth.models import AbstractUser


class Atividade(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("em andamento", "Em Andamento"),
        ("finalizada", "Finalizada"),
    ]

    materia = models.CharField(max_length=255)
    conteudo = models.TextField()
    prazo = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")



    def __str__(self):
        return f"{self.materia} - {self.conteudo}"


