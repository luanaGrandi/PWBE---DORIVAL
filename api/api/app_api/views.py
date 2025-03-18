from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def read_carros(request):
    carros = Carro.objects.all()
    serializer = CarroSerializers(carros, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializers(carro)
    return Response(serializer.data)


@api_view(['POST']) #criar
def create_carro(resuest):
    if resuest.method == 'POST':
        serializer = CarroSerializers(data = resuest.data, many=isinstance(resuest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializers(carro, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)


@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
       return Response({'Erro': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    carro.delete()
    return Response({'Mensagem': f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)
