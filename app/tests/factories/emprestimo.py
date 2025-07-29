import factory 

from core.models import Emprestimo

from uuid import uuid4

from datetime import datetime, timedelta

from . import LivroFactory, UsuarioFactory

class EmprestimoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Emprestimo
    
    id = factory.LazyFunction(uuid4)
    usuario = factory.SubFactory(UsuarioFactory)
    livro = factory.SubFactory(LivroFactory)
    emprestado_em = factory.Faker('date_between', start_date='-30d', end_date='today')
    vencimento_em = factory.LazyAttribute(lambda o: o.emprestado_em + timedelta(days=7))
    devolvido_em = factory.Maybe(
        '0.8', 
        yes_declaration=factory.LazyAttribute(
            lambda o: factory.Faker().date_between(start_date=o.emprestado_em, end_date=datetime.now().date())
        ),
        no_declaration=None
    )
    