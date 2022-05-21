from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuario(request):
     # Verifica se é do tipo Post
    if(request.method == "POST"):
        # O Django já tem um metodo de autenticação
        # Então usa o UserCreationForm, onde possui todo o processo de validação
        # É passado a requisição
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            # Se for valido, então salva no banco de dados
            form_usuario.save()
            return redirect('listar_tarefas')
    else:
        # Cria uma instacia vazia
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Faz a autenticacao do usuario e se tiver então retorna o usuaio
        usuario = authenticate(request, username=username, password=password)
        # Se o usuario não for vazio
        if usuario is not None:
            login(request, usuario)
            return redirect ('listar_tarefas')
        # Se o usuario for vazio então retorna uma mensagem de erro
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html',{"form_login": form_login})

def deslogar_usuario(request):
    # Remove o usuario da sessao
    logout(request)
    return redirect('logar_usuario')