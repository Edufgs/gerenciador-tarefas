from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefa_service

# Gerencia as requisições do projeto.
# request = recebe uma requisição, tentativa de acessar
@login_required() # Vai privar o metodo só para usuarios logados
def listar_tarefas(request):
    tarefas = tarefa_service.listar_tarefas(request.user)
    # Não precisa falar a pasta templates, pois o django ja sabe.
    # Esse metodo vai renderizar o arquivo listar_tarefas.html
    # {"nome_tarefa": nome_tarefa} = manda a variavel para a pagina html (listar_tarefas.html)
    return render(request, 'tarefas/listar_tarefas.html',{"tarefas": tarefas})

@login_required() # Vai privar o metodo só para usuarios logados
def cadastrar_tarefa(request):
    form_tarefa = TarefaForm()
    # Verifica se é do tipo Post
    if request.method == "POST":
        # Pega os dados da requisicao
        form_tarefa = TarefaForm(request.POST)
        # Se  for valido
        if form_tarefa.is_valid():
            # Pegas os dados do formulario
            titulo = form_tarefa.cleaned_data["titulo"]
            descricao = form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]
            # Cria o objeto tarefa
            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade, usuario=request.user)
            # Manda para cadastrar tarefa e cadasta no banco de dados
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            # Redireciona para a pagina de listar tarefas
            return redirect('listar_tarefas') 
    # Se não for do tipo post    
    else:
        # Cria um formulaio vazio
        form_tarefa = TarefaForm()
            
    # Envia {"form_tarefa": form_tarefa}) para o template
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

@login_required() # Vai privar o metodo só para usuarios logados
def editar_tarefa(request,id):
    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    # verifica se o usuario da tarefa é o mesmo que esta logado
    if tarefa_bd.usuario != request.user:
        # Retirna uma pagina HTML pura com o texto
        return  HttpResponse("Não permitido")
    # Vai criar um formulaio com os dados da tarefa
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_bd)
    # VErifica se a tarefa é valida
    if form_tarefa.is_valid():
        # Pegas os dados do formulario
        titulo = form_tarefa.cleaned_data["titulo"]
        descricao = form_tarefa.cleaned_data["descricao"]
        data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
        prioridade = form_tarefa.cleaned_data["prioridade"]
        # Cria o objeto tarefa
        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade, usuario=request.user)
        # Manda a tarefa antiga e a nova no banco para editar a tarefa no banco
        tarefa_service.editar_tarefa(tarefa_bd,tarefa_nova)
        # Redireciona para a pagina de listar tarefas
        return redirect('listar_tarefas')
    # Envia {"form_tarefa": form_tarefa}) para o template
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

@login_required() # Vai privar o metodo só para usuarios logados
def remover_tarefa(request,id):
    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    # verifica se o usuario da tarefa é o mesmo que esta logado
    if tarefa_bd.usuario != request.user:
        # Retirna uma pagina HTML pura com o texto
        return  HttpResponse("Não permitido")
    if request.method == "POST":
        tarefa_service.remover_tarefa(tarefa_bd)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html', {"tarefa": tarefa_bd})