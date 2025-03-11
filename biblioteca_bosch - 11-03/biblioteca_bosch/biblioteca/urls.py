from django.urls import path
from . import views

urlpatterns = [
 path('', views.lista_livros, name='lista_livros'),
 path('criar/', views.criar_livro, name='criar_livro'),
 path('editar/<int:pk>/', views.editar_livro, name='editar_livro' ),
 path('deletar/<int:pk>/', views.deletar_livro, name= 'deletar_livro'),
 path('filtro/', views.filtro_livros, name= 'filtro_livros'),
]

