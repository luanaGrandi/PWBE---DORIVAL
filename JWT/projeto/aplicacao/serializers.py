from rest_framework import serializers
from .models import UsuarioDS16

# transformar todos os dados do  UsuarioDS16 em json
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = '__all__'