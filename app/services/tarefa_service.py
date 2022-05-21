from ..models import Tarefa

# Responsavel por cadastar a tarefa no banco de dados.
def cadastrar_tarefa(tarefa):
    # Cria a tarefa com os atributos passado
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao, data_expiracao=tarefa.data_expiracao, prioridade=tarefa.prioridade, usuario=tarefa.usuario)

def listar_tarefas(usuario):
    # Retorna todas as tarefas do banco de dados e filtra o usuario
    return Tarefa.objects.filter(usuario=usuario).all()

def listar_tarefa_id(id):
    # Retorna a tarefa do banco de dados com o id passado
    return Tarefa.objects.get(id=id)

def editar_tarefa(tarefa_bd, tarefa_nova):
    # Atualiza os dados da tarefa
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.prioridade = tarefa_nova.prioridade
    # Salva no banco e forca a atualizar
    tarefa_bd.save(force_update=True)
    
def remover_tarefa(tarefa_bd):
    # Remove a tarefa do banco de dados
    tarefa_bd.delete()