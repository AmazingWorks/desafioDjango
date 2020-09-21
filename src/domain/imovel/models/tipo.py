from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=30)
