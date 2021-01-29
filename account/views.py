from django.shortcuts import render


def cria_conta(request):
    return render(request, 'account/cadastro.html')


def entrar_app(request):
    return render(request, 'account/entrar.html')


def sair_app(request):
    return render(request, 'account/sair.html')
