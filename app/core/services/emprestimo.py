from django_inscode.services import OrchestratorService, GenericModelService

from django_inscode import exceptions, mixins

from core.repositories import livro_repository, usuario_repository, emprestimo_repository
from core.schemas import EmprestimoSchema

class EmpretimoService(GenericModelService, mixins.ServiceReadMixin):
    pass


class RealizarEmprestimoService(OrchestratorService):
    def execute(self, request, *args, **kwargs):
        livro_id = request.data.get("livro")
        usuario_id = request.data.get("usuario")
    
        try:
            usuario = usuario_repository.read(usuario_id)
        except exceptions.NotFound:
            raise exceptions.NotFound(message="Usuário não encontrado.")
        
        try:
            livro = livro_repository.read(livro_id)
        except exceptions.NotFound:
            raise exceptions.NotFound(message="Livro não encontrado")
        
        emprestimo = emprestimo_repository.create(livro=livro, usuario=usuario)

        return EmprestimoSchema().dump(emprestimo)

emprestimo_service = EmpretimoService(emprestimo_repository)
realizar_emprestimo_service = RealizarEmprestimoService()

