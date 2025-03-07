from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserCostumizado(AbstractUser):
    def __str__(self):
        return self.username
    
class Perfil(models.Model):
    usuario = models.OneToOneField(UserCostumizado, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    data_nascimento = models.DateField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.usuario.username

class Atividade(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    estudante = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="atividades")
    materia = models.CharField(max_length=100)
    conteudo = models.TextField()
    prazo = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.materia
    
    
    