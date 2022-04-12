from django.shortcuts import render
from .forms import AccountCreationForm, AccountChangeForm, AccountLoginForm


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
    else:
        form = AccountCreationForm
    contexto = {'form': form}
    return render(request, 'account/register.html', contexto)


def login(request):
    form = AccountLoginForm()
    contexto = {'form': form}
    return render(request, 'account/login.html', contexto)


def logout(request):
    return render(request, 'account/logout.html')
