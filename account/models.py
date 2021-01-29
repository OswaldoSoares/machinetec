from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    UsuarioNivel = models.CharField(max_length=20, default='BASICO')
