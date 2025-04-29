from django.contrib import admin
from .models import Ingresso, Usuario, Empresa
from django.contrib.auth.admin import UserAdmin


class UsuarioAdmin(UserAdmin):
    # VER AS INFROMAÇÕES. ELE É COMO O GET, POST E PATCH
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }), 
    )
    # ESSE AQUI É PARA CRIAR UM USUARIO
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }), 
    )


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Ingresso)
admin.site.register(Empresa)

