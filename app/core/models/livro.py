from django.db import models

from django_inscode.models import SoftDeleteBaseModel

class Livro(SoftDeleteBaseModel):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    publicado_em = models.DateField()

    @property
    def is_emprestado(self):
        return self.emprestimos.filter(devolvido_em__isnull=True).exists()