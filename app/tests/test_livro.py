from django.test import TestCase, Client
from django.urls import reverse

from .factories import LivroFactory


class LivroTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.livro = LivroFactory(titulo="livro teste")
        self.livro2 = LivroFactory(titulo="livro outro")
    
    def test_create_livro(self):
        response = self.client.post(reverse('livro'), {
            'titulo': 'test',
            'autor': 'test',
            'editor': 'teste',
            'publicado_em': '2023-10-01'
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue('id' in response.json())
    
    def test_filter_livro_by_titulo(self):
        response = self.client.get(reverse('livro'), {'titulo': 'teste'})

        self.assertEqual(response.status_code, 200)

        results = response.json()['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['titulo'], 'livro teste')