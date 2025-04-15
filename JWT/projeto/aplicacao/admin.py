from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    # lista do usuario
    list_display = ('nome', 'biografia', 'idade', 'telefone', 'endereco', 'animais')

    # qual campo ele vai comstrar quando clicar no usuario
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('idade', 'telefone', 'biografia')}),
    )

    # campos que vai aparecer quando for criar um novo usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('idade', 'telefone', 'biografia', 'endereco', 'animais', 'categoria')}),
)
admin.site.register(UsuarioDS16, UsuarioDS16Admin)