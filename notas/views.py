from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import NotaForm
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

@login_required(login_url='usuarios:login')
def home(request):
    return render(request, 'home.html')


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