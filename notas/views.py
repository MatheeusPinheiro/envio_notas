from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Nota

# Create your views here.

@login_required(login_url='usuarios:login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='usuarios:login')
def cadastrar_nota(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_nota.html')
    elif request.method == 'POST':
        
        nome_razao_social = request.POST.get('nome_razao_social')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        municipio = request.POST.get('nome_razao_social')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cnpj_cpf = request.POST.get('cnpj_cpf')
        iscricao_estadual = request.POST.get('iscricao_estadual')
        desc_produto = request.POST.get('desc_produto')
        quantidade = request.POST.get('quantidade')
        valor_unitario = request.POST.get('nome_razao_social')
        valor_total = request.POST.get('valor_total')

        

        return HttpResponse(f'{nome_razao_social}')
        