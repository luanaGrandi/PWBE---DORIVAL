from django.urls import path
from . import views

urlpatterns = [
    path('usuario/criarAdm/', view=views.criar_usuario, name='criar_usuario'),
    path('usuario/logar/', view=views.logar_usuario, name='logar_usuario' ),
    path('usuario/listar/',  view=views.listar_usuario, name='listar_usuario'),
    path('usuario/criarUsuario/',  view=views.create_usuario, name='create_usuario'),
    path('usuario/atualizar/<int:pk>',  view=views.update_usuario, name='update_usuario'),
    path('usuario/apagar/<int:pk>',  view=views.delete_usuario, name='delete_usuario'),
]






# {
# "username": "luana",
# "senha": "2008"
# }