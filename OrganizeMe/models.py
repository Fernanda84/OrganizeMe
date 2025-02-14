from django.db import models

class Atividade(models.Model):
    materia = models.CharField(max_length=200)
    assunto = models.TextField(max_length=200)
    prazo = models.DateField(max_length=100)
    status = models.CharField(max_length=50, default='Em andamento')

    def __str__(self):
        return f"{self.materia} - {self.status}"

 
    