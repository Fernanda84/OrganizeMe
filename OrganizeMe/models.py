from django.db import models

class Atividade(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    materia = models.CharField(max_length=100)
    conteudo = models.TextField()
    prazo = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.materia