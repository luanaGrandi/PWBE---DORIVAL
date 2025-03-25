from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# função para ler os carros cadastrados e listar ele para o usuario
@api_view(['GET'])
def read_carros(request):
    carros = Carro.objects.all()
    serializer = CarroSerializers(carros, many = True)
    return Response(serializer.data)

# função para procurar um determinado carro atraves da sua ID
@api_view(['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    # se o carro não existir mostrar essa mensagem de erro
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializers(carro)
    return Response(serializer.data)

# funçõa para fazer a criação de novos carros 
@api_view(['POST']) #criar
def create_carro(resuest):
    if resuest.method == 'POST':
        serializer = CarroSerializers(data = resuest.data, many=isinstance(resuest.data, list))
        # analizar se a criação foi valida
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# funçõa para atualizar as informaçoes dos carros ja cadastrdos
@api_view(['PUT'])
def update_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    # se o carro não existir ou não for achado, exibir esssa mensagem de erro
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializers(carro, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)


# funçõa para deletra o carro escolhido atraves do seu ID
@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    #se o carro não existe ou ele ja foi apagado, exxibir essa mensagem 
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    # para saber se o carro foi deletado, exibir essa mensagem
    carro.delete()
    return Response({'Mensagem': f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)
