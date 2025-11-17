from django.db import models

class Atividade(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
    ]

    materia = models.CharField(max_length=100)
    conteudo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    prazo = models.DateField()
    concluida = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.materia} - {self.conteudo[:20]}'

