import io
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Produto, Venda
import pandas as pd


class ProdutoViewsTest(TestCase):
    def setUp(self):
        # Configurando o cliente para simular requisições HTTP
        self.client = Client()
        # Criando um produto para ser usado nos testes
        self.produto = Produto.objects.create(
            codigo='P001',
            nome='Produto Teste',
            quantidade_estoque=100,
            preco_unidade=10.00
        )

    def test_listar_produtos(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto_list.html')
        self.assertContains(response, 'Produto Teste')

    def test_criar_produto(self):
        data = {
            'codigo': 'P002',
            'nome': 'Novo Produto',
            'quantidade_estoque': 50,
            'preco_unidade': 15.00
        }
        response = self.client.post(reverse('criar_produto'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Produto.objects.filter(nome='Novo Produto').exists())

    def test_editar_produto(self):
        data = {
            'codigo': 'P001',
            'nome': 'Produto Editado',
            'quantidade_estoque': 80,
            'preco_unidade': 12.00
        }
        response = self.client.post(reverse('editar_produto', args=[self.produto.id]), data)
        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Editado')

    def test_excluir_produto(self):
        response = self.client.post(reverse('excluir_produto', args=[self.produto.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())


class VendaViewsTest(TestCase):
    def setUp(self):
        # Criando cliente e produto para testes de vendas
        self.client = Client()
        self.produto = Produto.objects.create(
            codigo='P001',
            nome='Produto Teste',
            quantidade_estoque=100,
            preco_unidade=10.00
        )

    def test_registrar_venda_estoque_suficiente(self):
        data = {
            'produto': self.produto.id,
            'quantidade_vendida': 5
        }
        response = self.client.post(reverse('registrar_venda'), data)
        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade_estoque, 95)
        self.assertTrue(Venda.objects.filter(produto=self.produto, quantidade_vendida=5).exists())

    def test_registrar_venda_estoque_insuficiente(self):
        data = {
            'produto': self.produto.id,
            'quantidade_vendida': 200
        }
        response = self.client.post(reverse('registrar_venda'), data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(messages[0]), 'Quantidade insuficiente no estoque!')
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade_estoque, 100)  # Estoque não muda


class RelatoriosTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produto = Produto.objects.create(
            codigo='P001',
            nome='Produto Teste',
            quantidade_estoque=100,
            preco_unidade=10.00
        )
        self.venda = Venda.objects.create(produto=self.produto, quantidade_vendida=10)

    def test_gerar_relatorio_csv(self):
        response = self.client.get(reverse('relatorio_vendas'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="relatorio_vendas.csv"')

        # Usando StringIO para converter o conteúdo em um buffer
        csv_content = io.StringIO(response.content.decode('utf-8'))

        # Validar conteúdo do CSV usando pandas
        df = pd.read_csv(csv_content)
        self.assertEqual(df.iloc[0]['Nome do produto'], 'Produto Teste')
        self.assertEqual(df.iloc[0]['Quantidade vendida'], 10)

    def test_gerar_relatorio_estoque(self):
        response = self.client.get(reverse('relatorio_estoque'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="relatorio_estoque.txt"')

        conteudo = response.content.decode('utf-8')
        self.assertIn('Código: P001', conteudo)
        self.assertIn('Nome: Produto Teste', conteudo)
        self.assertIn('Quantidade em estoque: 100', conteudo)
