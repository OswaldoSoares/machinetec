from django.urls import path
from .views import cria_conta, entrar_app, sair_app


urlpatterns = [
    path('cadastro/', cria_conta, name='cria_conta'),
    path('entrar/', entrar_app, name='entrar_app'),
    path('sair/', sair_app, name='sair_app'),
]