from rest_framework import serializers
from .models import Usuario, Empresa, Ingresso
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    # serializar os dados do models
    class Meta:
        model = Usuario
        # pegar todas as informações
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    # serializar os dados do models
    class Meta:
        model = Empresa
        # pegar todas as informações
        fields = '__all__'


class LoginSerializer (TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # super -> vai chamar a validação do token 
        data['usuario'] = {
            'id': self.user.id,
            'username': self.user.username,
            
        }
        return data
    
class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'
        