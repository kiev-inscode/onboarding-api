from django.urls import path

from .views import LivroView, UsuarioView


urlpatterns = [
    path("livro/", LivroView.as_view(), name="livro"),
    path("usuario/", UsuarioView.as_view(), name="usuario")
]