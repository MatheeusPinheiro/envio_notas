from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import NotaForm
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

@login_required(login_url='usuarios:login')
def home(request):
    notas = Nota.objects.all()
    context = {'notas': notas}
    return render(request, 'home.html', context)


@login_required(login_url='usuarios:login')
def cadastrar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Nota Fiscal cadastrada com sucesso.')
            return redirect('notas:home')  # Corrigir para usar return
    else:
        form = NotaForm()

    return render(request, 'cadastrar_nota.html', {'form': form})



@login_required(login_url='usuarios:login')
def detalhe_nota(request, id):
    nota = get_object_or_404(Nota, pk=id)  # Obtém a nota com base no id fornecido
    context = {'nota': nota}
    return render(request, 'detalhe_nota.html', context)