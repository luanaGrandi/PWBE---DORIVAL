from rest_framework import serializers
from .models import Piloto, Carro
# importação das models e do serializer

# class PilotoSerializer para transformar os dados da models Piloto em json
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

# class CarroSerializer para transformar os dados da models Carro em json
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'