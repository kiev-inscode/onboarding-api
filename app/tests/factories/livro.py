import factory 

from core.models import Livro

from uuid import uuid4

class LivroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Livro
    
    id = factory.LazyFunction(uuid4)
    titulo = factory.Faker('sentence', nb_words=3)
    autor = factory.Faker('name')
    editor = factory.Faker('company')
    publicado_em = factory.Faker('date')
    