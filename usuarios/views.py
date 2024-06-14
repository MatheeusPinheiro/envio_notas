from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib import messages
from django.contrib import auth
from django.contrib.messages import constants
from django.urls import reverse
# Create your views here.


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        #Verifca se as senhas digitadas são iguais
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas digitadas não são iguais!')
            return redirect('usuarios:cadastro') #auth/cadastro/
        
        #Verifica se já existe um usuario com esse nome no sistema
        user = User.objects.filter(username=username).first()
        if user:
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome no sistema.')
            return redirect('usuarios:cadastro') #auth/cadastro/
        
        #cadastra o usuário no sistema 
        try:

            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )

            messages.add_message(request, constants.ERROR, 'Usuário cadastrado com sucesso.')
            return redirect('usuarios:login')
        
        except Exception as ex:
            messages.add_message(request, constants.ERROR, f'Erro interno no sistema {ex}.')
            return redirect('usuarios:cadastro')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django(request, user)
            return redirect('notas:home')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos!')
            return redirect('usuarios:login')
        


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect(reverse('usuarios:login'))