from django.db import models

class Teste(models.Model):
    Des = models.CharField(max_length=20)
    Tempo = models.DurationField(default=0)

