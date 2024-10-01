from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms.produto_form import ProdutoForm


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
