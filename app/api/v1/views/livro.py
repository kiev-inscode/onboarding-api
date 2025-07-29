from django_inscode.views import ModelView

from core.services import livro_service
from core.schemas import LivroSchema
from core.filters import LivroFilter


class LivroView(ModelView):
    service = livro_service
    serializer = LivroSchema
    fields = ["titulo", "autor", "publicado_em", "editor"]
    filter_class = LivroFilter