from django.db import models

from django_inscode.models import SoftDeleteBaseModel


class Emprestimo(SoftDeleteBaseModel):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name="emprestimos", blank=False)
    livro = models.ForeignKey("Livro", on_delete=models.CASCADE, related_name="empretimos")

    class Meta:
        pass

