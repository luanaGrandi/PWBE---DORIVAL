from django.shortcuts import render
from .models import Tarefas

def listaTarefas(request):
    tarefas = Tarefas.objects.all().order_by('-data_criacao')
    return render(request, 'lista/listaTarefas.html', {'tarefas': tarefas})
