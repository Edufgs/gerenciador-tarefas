from django.db import models
from django.contrib.auth.models import User

# Determinada todas as classes do projeto
# Vai ser migrada para o banco de dados
# A chave primaria(id) será gerada automaticamente pelo comando
# Usa o comando "python3 manage.py makemigrations" para criar as migrations
class Tarefa(models.Model):
    # CHOICES são lista de opções que podem ser escolhidas
    PRIOREIDADE_CHOICES = [
        ('A', 'Alta'),
        ('N', 'Normal'),
        ('B', 'Baixa'),
    ]
    # Campo de String onde o maximo de caractereé 30, não pode ser nulo e nem vazio (blank=False)
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    # Vai ser definido as prioridade alta, normal e baixa.
    prioridade  = models.CharField(max_length=1, choices=PRIOREIDADE_CHOICES, null=False, blank=False)
    # Vai fazer referencia com um usuario
    # ForeignKey = Relacionamento de 1 para N
    # User = O ForeignKey vai fazer referencia com a tabela User do django
    # null=True = Diz que pode ter dados nulos pois se tiver tarefas no banco então vai estar com essa coluna nula
    # on_delete=models.CASCADE = Diz que se um usuario for deletado então é apagado as tarefas dele
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    