from django_inscode.services import ModelService

from core.repositories import usuario_repository

class UsuarioService(ModelService):
    pass

usuario_service = UsuarioService(usuario_repository)