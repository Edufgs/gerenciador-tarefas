"""gerenciador_tarefas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views.usuario_views import *
from .views.tarefa_views import *

# Vai ter todas as urls do projeto.

urlpatterns = [
    # Se entrar dentro da URL listar_tarefas, vai chamar a função listar_tarefas.
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    # Para editar precisa receber o id da tarefa.
    # O nome id tem que ser igual ao nome da variável que está no metodo editar_tarefa na views.
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]
