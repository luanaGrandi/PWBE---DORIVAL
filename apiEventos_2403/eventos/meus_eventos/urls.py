from django.urls import path
from . import views

# essa parte é o caminho para chegar na onde precisa
urlpatterns = [
    # caminho para mostrar todos os eventos
    path('eventos/', views.read_eventos),
    # caminho para procurar os eventos pelo ID
    path('eventos/buscar/<int:pk>', views.pegar_eventos),
    # caminho para criar novos enventos
    path('eventos/criar/', views.create_eventos),
    # caminho para atualizar as informações do evento
    path('eventos/atualizar/<int:pk>', views.update_eventos),
    # caminho para deletar eventos ja cadastrados
    path('eventos/apagar/<int:pk>', views.delete_eventos),
    path('eventos/proximos/', views.proximos_eventos),
]
