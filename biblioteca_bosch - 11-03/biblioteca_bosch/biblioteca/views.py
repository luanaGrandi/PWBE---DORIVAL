from django.shortcuts import render,redirect,get_object_or_404
from .models import Cadastro
from .forms import CadastroForm


# função para aparecer os livros na tela inical
def lista_livros(request):
    cadastro = Cadastro.objects.all().order_by('-ano')
    return render(request, 'biblioteca/lista_livros.html', {'cadastro': cadastro})

# função para fazer o funcionamento de deletar o livro escolhido
def deletar_livro(request, pk):
    livro = get_object_or_404(Cadastro, pk = pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'biblioteca/deletar_livro.html', {'livro': livro})

# função para fazer o funcionamento de editar o livro escolhido
def editar_livro(request, pk):
    livro = get_object_or_404(Cadastro, pk = pk)
    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = CadastroForm(instance=livro)
    return render(request, 'biblioteca/criar_livro.html', {'form': form})

# função para fazer o funcionamento de criar/ cadstrar um livro novo
def criar_livro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = CadastroForm()
    return render(request, 'biblioteca/criar_livro.html', {'form': form})

# função para  fazer o funcionamento do flitro atraves do titulo do livro
def filtro_livros(request):
    titulo = request.GET.get('titulo', '')
    # autor = request.GET.get('autor', None)
   
    if titulo:
        titulo = Cadastro.objects.filter(titulo__icontains = titulo) 
        print(titulo)
    # if autor:
    #     livro = livro.filter(autor__icontains=autor)
    else:
        titulo = Cadastro.objects.all()
    return render(request, 'biblioteca/lista_livros.html', {'cadastro': titulo})



