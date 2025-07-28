from django_inscode.services import OrchestratorService, GenericModelService

from django_inscode import exceptions, mixins

from core.repositories import livro_repository, usuario_repository, emprestimo_repository
from core.schemas import EmprestimoSchema

from datetime import datetime

class EmpretimoService(GenericModelService, mixins.ServiceReadMixin):
    pass

class RealizarEmprestimoService(OrchestratorService):
    def execute(self, request, *args, **kwargs):
        livro_id = request.data.get("livro")
        usuario_id = request.data.get("usuario")

        try:
            livro = livro_repository.read(livro_id)
        except exceptions.NotFound:
            raise exceptions.NotFound(message="Livro não encontrado")

        if livro.is_emprestado:
            raise exceptions.ValidationError(message="Livro já emprestado.")
    
        try:
            usuario = usuario_repository.read(usuario_id)
        except exceptions.NotFound:
            raise exceptions.NotFound(message="Usuário não encontrado.")
        
        emprestimo = emprestimo_repository.create(livro=livro, usuario=usuario)

        return EmprestimoSchema().dump(emprestimo)

class DevolverEmprestimoService(OrchestratorService):
    def execute(self, request, emprestimo_id, *args, **kwargs):

        try:
            emprestimo = emprestimo_repository.read(emprestimo_id)
        except exceptions.NotFound:
            raise exceptions.NotFound(message="Empréstimo não encontrado.")

        if emprestimo.devolvido_em is not None:
            raise exceptions.ValidationError(message="Livro já devolvido.")

        emprestimo_updated = emprestimo_repository.update(emprestimo_id, devolvido_em=datetime.now().date())

        return EmprestimoSchema().dump(emprestimo_updated)

emprestimo_service = EmpretimoService(emprestimo_repository)
realizar_emprestimo_service = RealizarEmprestimoService()
devolver_emprestimo_service = DevolverEmprestimoService()

