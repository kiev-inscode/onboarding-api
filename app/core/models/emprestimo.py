from django.db import models

from django_inscode.models import SoftDeleteBaseModel

from datetime import datetime, timedelta


class Emprestimo(SoftDeleteBaseModel):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name="emprestimos", blank=False)
    livro = models.ForeignKey("Livro", on_delete=models.CASCADE, related_name="emprestimos", blank=False)
    emprestado_em = models.DateField(auto_now_add=True)
    vencimento_em = models.DateField(default=datetime.now().date()+timedelta(days=7))
    devolvido_em = models.DateField(default=None, null=True, blank=True)

    class Meta:
        pass

    @property
    def is_atrasado(self):
        if self.devolvido_em:
            return False
        
        return datetime.now().date() > self.vencimento_em


