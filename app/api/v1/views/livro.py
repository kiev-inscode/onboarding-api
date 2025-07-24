from django_inscode.views import ModelView

from core.services import livro_service
from core.transports import LivroTransport


class LivroView(ModelView):
    service = livro_service
    serializer = LivroTransport
    fields = ["titulo", "autor", "publicado_em", "editor"]