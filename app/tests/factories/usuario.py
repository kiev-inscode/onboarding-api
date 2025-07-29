import factory 

from core.models import Usuario

from uuid import uuid4

class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario
    
    id = factory.LazyFunction(uuid4)
    nome = factory.Faker('name')
    idade = factory.Faker('random_int', min=8, max=120)
    email = factory.Faker('email')
    