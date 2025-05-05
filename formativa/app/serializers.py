from rest_framework import serializers
from .models import Usuario, Disciplina, ReservaAmbiente
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializere):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

# autenticação do login
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    senha = serializers.CharField(write_only = True)

    # validar os dados, ver se o nome e senha estão corretos
    def validate(self, attrs):
        data =  super().validate(attrs)

        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo
        }
        return data
    