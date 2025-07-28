from django_inscode.views import ModelView

from core.services import usuario_service
from core.schemas import UsuarioSchema


class UsuarioView(ModelView):
    service = usuario_service
    serializer = UsuarioSchema
    fields = ["nome", "idade", "email"]