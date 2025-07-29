from django_inscode.views import ModelView

from core.services import usuario_service
from core.schemas import UsuarioSchema
from core.filters import UsuarioFilter


class UsuarioView(ModelView):
    service = usuario_service
    serializer = UsuarioSchema
    fields = ["nome", "idade", "email"]
    filter_class = UsuarioFilter