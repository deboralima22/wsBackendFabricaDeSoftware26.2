import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'app/lista_produtos.html', {'produtos': produtos})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'app/form_produto.html', {'form': form})


def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'app/form_produto.html', {'form': form})


def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'app/confirmar_delete.html', {'produto': produto})


def consultar_cep(request):
    resultado = None
    erro = None

    if request.method == 'POST':
        cep = request.POST.get('cep', '').replace('-', '').strip()

        if not cep.isdigit() or len(cep) != 8:
            erro = 'CEP inválido. Digite 8 números, ex: 01310100'
        else:
            try:
                resposta = requests.get(
                    f'https://viacep.com.br/ws/{cep}/json/',
                    timeout=5
                )

                if resposta.status_code == 200:
                    dados = resposta.json()
                    if dados.get('erro'):
                        erro = 'CEP não encontrado.'
                    else:
                        resultado = dados
                else:
                    erro = f'A API retornou um erro (status {resposta.status_code}).'

            except requests.exceptions.Timeout:
                erro = 'A API demorou demais para responder. Tente novamente.'
            except requests.exceptions.ConnectionError:
                erro = 'Não foi possível conectar à API. Verifique sua internet.'
            except requests.exceptions.RequestException as e:
                erro = f'Ocorreu um erro inesperado: {e}'

    return render(request, 'app/consultar_cep.html', {'resultado': resultado, 'erro': erro})