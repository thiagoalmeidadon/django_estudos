from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar sua mensagem!')

    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else :
            messages.error(request, 'Produto Erro!')
    else :
        form = ProdutoModelForm()
    context = {
        'form' : form
    }
    return render(request, 'produto.html', context)