from atexit import register
from re import template
from django import template

# Template para criar filtros para o template
register = template.Library()

# Recebe uma valor e argumento
# É preciso registar com um nome
@register.filter(name='addclass')
def addclass(value, arg):
    # Retorna o valor com a classe adicionada em arg
    return value.as_widget(attrs={'class': arg})