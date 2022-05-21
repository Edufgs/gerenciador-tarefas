from django.apps import AppConfig

# Algumas configurações da aplicação.

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
