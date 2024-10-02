from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
