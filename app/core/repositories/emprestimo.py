from django_inscode.repositories import Repository

from core.models import Emprestimo

class EmpretimoRepository(Repository):
    pass

emprestimo_repository = EmpretimoRepository(Emprestimo)