from django.urls import path
from . import views

# os caminhos para acessar as funções
urlpatterns = [
    # caminho para a listagem dos carros
    path('carros/', views.read_carros),
    # caminho para a busca dos carros cadastrados
    path('carros/buscar/<int:pk>', views.pegar_carro),
    # caminho para criar novos carros
    path('carros/criar/', views.create_carro),
    # caminho para atualizar as informaçoes dos carros cadastrados
    path('carros/atualizar/<int:pk>', views.update_carro),
    # caminho para apagar os carros
    path('carros/apagar/<int:pk>', views.delete_carro),
]