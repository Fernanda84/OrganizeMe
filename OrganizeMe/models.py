from django.db import models 

class Atividade(models.Model):
    materia = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    prazo = models.DateField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

 
    