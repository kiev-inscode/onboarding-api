from django_inscode.repositories import Repository

from core.models import Usuario

class UsuarioRepository(Repository):
    pass

usuario_repository = UsuarioRepository(Usuario)