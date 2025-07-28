from django_inscode.views import GenericOrchestratorView, GenericModelView

from django_inscode import mixins

from core.schemas import EmprestimoSchema
from core.services import emprestimo_service, realizar_emprestimo_service

class EmprestimoView(GenericModelView, mixins.ViewRetrieveModelMixin):
    serializer = EmprestimoSchema
    service = emprestimo_service

class RealizarEmprestimoView(GenericOrchestratorView):
    service = realizar_emprestimo_service

    def post(self, request, *args, **kwargs):
        return self.execute(request, *args, **kwargs)