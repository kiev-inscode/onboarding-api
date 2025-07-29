from django_inscode.views import GenericOrchestratorView, GenericModelView

from django_inscode import mixins

from core.filters import EmprestimoFilter
from core.schemas import EmprestimoSchema
from core.services import emprestimo_service, realizar_emprestimo_service, devolver_emprestimo_service

class EmprestimoView(GenericModelView, mixins.ViewRetrieveModelMixin):
    serializer = EmprestimoSchema
    service = emprestimo_service
    filter_class = EmprestimoFilter

class RealizarEmprestimoView(GenericOrchestratorView):
    service = realizar_emprestimo_service

    def post(self, request, *args, **kwargs):
        return self.execute(request, *args, **kwargs)
    
class DevolverEmprestimoView(GenericOrchestratorView):
    service = devolver_emprestimo_service

    def get(self, request, emprestimo_id, *args, **kwargs):
        return self.execute(request, *args, emprestimo_id=emprestimo_id, **kwargs)