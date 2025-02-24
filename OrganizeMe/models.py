from django.db import models


class Tarefa(models.Model):
    materia = models.CharField(max_length=100)
    conteudo = models.TextField()
    status_choices = [
        ('pendente', 'Pendente'),
        ('em andamento', 'Em Andamento'),
        ('finalizada', 'Finalizada'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pendente')
    prazo = models.DateField()


    def __str__(self):
        return self.materia


