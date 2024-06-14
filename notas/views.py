from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Nota

# Create your views here.

@login_required(login_url='usuarios:login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='usuarios:login')
def cadastrar_nota(request):
    if request.method == 'GET':
        ufs = Nota.objects.values_list('uf', flat=True)
        print(ufs)
        return render(request, 'cadastrar_nota.html')
    elif request.method == 'POST':
        pass