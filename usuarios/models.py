from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    foto = models.ImageField(blank=True)
    bio = models.TextField(max_length=2000, blank=True)

    def get_socials(self):
        return {
            "instagram": self.instagram,
            "facebook": self.facebook,
            "github": self.github
        }

    def __str__(self):
        return self.usuario.username
