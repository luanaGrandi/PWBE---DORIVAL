from django.urls import path
from . import views

# Rotas para as determinadas paginas
urlpatterns = [
    # rota do admin para criar usuario
    path('usuario/criarAdm/', view=views.criar_usuario, name='criar_usuario'),
    # rota para a pagina de logar o usuario para receber o token
    path('usuario/logar/', view=views.logar_usuario, name='logar_usuario' ),
    # rota para fazer a listagem de usuarios
    path('usuario/listar/',  view=views.listar_usuario, name='listar_usuario'),
    # rota para criar o usuario
    path('usuario/criarUsuario/',  view=views.create_usuario, name='create_usuario'),
    # rota para atualizar informações do usuario ja existente
    path('usuario/atualizar/<int:pk>',  view=views.update_usuario, name='update_usuario'),
    # rota para deletar os usuarios ja criados
    path('usuario/apagar/<int:pk>',  view=views.delete_usuario, name='delete_usuario'),
]






# {
# "username": "luana",
# "senha": "2008"
# }