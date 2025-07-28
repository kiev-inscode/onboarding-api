

from django_inscode.services import ModelService

from core.repositories import livro_repository


# from django_inscode.repositories import get_repository
# book_repository = get_repository("core.") ??

class LivroService(ModelService):
    pass

livro_service = LivroService(livro_repository)