from django.test import TestCase, Client
from django.urls import reverse

from .factories import UsuarioFactory


class UsuarioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = UsuarioFactory(nome="usuario teste")
        self.usuario2 = UsuarioFactory(nome="usuario outro", email="django@gmail.com")
    
    def test_create_usuario(self):
        response = self.client.post(reverse('usuario'), {
            'nome': 'test',
            'idade': 30,
            'email': 'teste@gmail.com'
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json())
    
    def test_filter_usuario_by_nome(self):
        response = self.client.get(reverse('usuario'), {'nome': 'teste'})

        self.assertEqual(response.status_code, 200)

        results = response.json()['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['nome'], 'usuario teste')
    
    def test_filter_usuario_by_email(self):
        response = self.client.get(reverse('usuario'), params={'email': 'django@gmail.com'})

        self.assertEqual(response.status_code, 200)

        results = response.json()['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['email'], 'django@gmail.com')