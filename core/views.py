from django.shortcuts import render

def index_core(request):
    return render(request, 'base.html')
