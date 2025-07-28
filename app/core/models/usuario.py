from django.db import models

from django_inscode.models import SoftDeleteBaseModel


class Usuario(SoftDeleteBaseModel):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    email = models.EmailField(unique=True)