from django.urls import path

from .views import LivroView, UsuarioView, EmprestimoView, RealizarEmprestimoView, DevolverEmprestimoView


urlpatterns = [
    path("livro/", LivroView.as_view(), name="livro"),
    path("usuario/", UsuarioView.as_view(), name="usuario"),
    path("emprestimo/", EmprestimoView.as_view(), name="emprestimo"),
    path("realizar_emprestimo/", RealizarEmprestimoView.as_view(), name="realizar_emprestimo"),
    path("devolver_emprestimo/<str:emprestimo_id>/", DevolverEmprestimoView.as_view(), name="devolver_emprestimo"),
]