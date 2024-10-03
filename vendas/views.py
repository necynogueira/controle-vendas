import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Produto, Venda
from .forms.produto_form import ProdutoForm
from .forms.venda_form import VendaForm


# Listar todos os produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto_list.html', {'produtos': produtos})


# Criar um novo produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})


# Editar um produto existente
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})


# Excluir um produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})


def registrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            produto = venda.produto

            if venda.quantidade_vendida > produto.quantidade_estoque:
                messages.error(request, 'Quantidade insuficiente no estoque!')
            else:
                # Atualiza o estoque
                produto.quantidade_estoque -= venda.quantidade_vendida
                produto.save()

                # Salva a venda
                venda.save()
                messages.success(request, 'Venda registrada com sucesso!')
                return redirect('registrar_venda')
    else:
        form = VendaForm()

    return render(request, 'registrar_venda.html', {'form': form})


def gerar_relatorio_csv(request):
    # Obtendo as vendas do banco de dados
    vendas = Venda.objects.select_related('produto').all()

    # Criando uma lista de dicionários com os dados para o CSV
    vendas_data = [
        {
            'Código do produto': venda.produto.codigo,
            'Nome do produto': venda.produto.nome,
            'Quantidade vendida': venda.quantidade_vendida,
            'Valor total da venda': venda.quantidade_vendida * venda.produto.preco_unidade,
        }
        for venda in vendas
    ]

    # Convertendo a lista de dicionários em um DataFrame do pandas
    df = pd.DataFrame(vendas_data)

    # Gerando o CSV em memória
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.csv"'
    df.to_csv(path_or_buf=response, index=False)

    return response


def gerar_relatorio_estoque(request):
    # Criando o conteúdo do arquivo de relatório
    produtos = Produto.objects.all()
    linhas_relatorio = []

    for produto in produtos:
        # Cria a tupla com os valores
        dados_produto = (produto.codigo, produto.nome, produto.quantidade_estoque)
        # Usa a tupla para formatar a linha
        linha = "Código: {}, Nome: {}, Quantidade em estoque: {}\n".format(*dados_produto)
        linhas_relatorio.append(linha)

    # Unindo as linhas em um único texto
    conteudo_relatorio = ''.join(linhas_relatorio)

    # Gerando a resposta como um arquivo de texto
    response = HttpResponse(conteudo_relatorio, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="relatorio_estoque.txt"'

    return response
