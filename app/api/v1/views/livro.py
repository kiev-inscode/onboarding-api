from django_inscode.views import ModelView

from core.services import livro_service
from core.schemas import LivroSchema


class LivroView(ModelView):
    service = livro_service
    serializer = LivroSchema
    fields = ["titulo", "autor", "publicado_em", "editor"]