from django.urls import path

from .views import LivroView


urlpatterns = [
    path("livro/", LivroView.as_view(), name="livro")
]