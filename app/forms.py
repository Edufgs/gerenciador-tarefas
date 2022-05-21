# Cria o formulario de cadastro e faz as validações

from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    # Classe Meta onde vai ser colcado onde vai ser inserido no banco de dados
    class Meta:
        # Diz qual model (Tarefa) vai ser usado
        model = Tarefa
        # Não vai permitir que o usuario seja selecionado e nois vai passar o usuario
        # Tb diz que o o formulario seja passado em um usuario selecionado manualmente
        exclude = ('usuario',)
        # Os campos que vai ser renderizado no formulario que vai ser todos        
        fields = '__all__'