from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

# ele ira ler todos os eventos cadastrado pelo usuario e listar os eventos
@api_view(['GET'])
def read_eventos(request):
    eventos = Evento.objects.all()
    
    # Filtrar os eventos pelo nome da categoria
    categorias = request.query_params.get('categoria')
    # Filtrar os eventos pela data e hora
    datas = request.query_params.get('dataHora')
    # filtrar os eventos pela quantidade
    quantidade = request.query_params.get('quantidades')
    # ordenar os eventos pelas suas datas
    ordenar = request.query_params.get('ordenar')

    # Filtrar os eventos pelo nome da categoria
    if categorias:
        eventos = eventos.filter(categoria__icontains = categorias)
    # Filtrar os eventos pela data e hora
    elif datas:
        eventos = eventos.filter(dataHora__icontains = datas)

    # Filtrar os eventos pela quantidade
    if quantidade:
        try:
            quantidade = int(quantidade)
            eventos = eventos[:quantidade]  
        except ValueError:
            return Response({"error": "O parâmetro 'quantidades' deve ser um número inteiro válido!"}, status=400)
        
     # ordenar os eventos pelas suas datas 
    if ordenar:
            eventos = eventos.order_by('datas').values()


    serializer = EventoSerializers(eventos, many = True)
    return Response(serializer.data)

# funçõa para filtrar os eventos que irão acontecer futuramente
@api_view(['GET'])
def proximos_eventos(request):
    data_atual = datetime.now()
    data_futura = data_atual + timedelta(days=7)

    try:
        evento = Evento.objects.all()  
    except Evento.DoesNotExist:
            return Response({"error": "Evento não encontrado!"}, status=404)
        
    # Filtrando eventos futuros relacionados ao evento
    eventos_proximos = Evento.objects.filter(dataHora__gte=data_atual, dataHora__lte=data_futura)
    # GTE = maior que / LTE = menor ou igual

    # Serializando os eventos
    serializer = EventoSerializers( eventos_proximos, many=True)
    return Response(serializer.data)


# ele ira busacar os enventos cadastrados atraves do seu Id
@api_view(['GET'])
def pegar_eventos(request, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
       return Response({'Erro': 'Evento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializers(eventos)
    return Response(serializer.data)

 #Criar novos eventos colocando todos os seus atibutos necessaios
@api_view(['POST'])
def create_eventos(resuest):
    if resuest.method == 'POST':
        serializer = EventoSerializers(data = resuest.data, many = isinstance(resuest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  atualizar os dados de um eventos ja existente atraves do ID
@api_view(['PUT'])
def update_eventos(request, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
       return Response({'Erro': 'Evento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializers(eventos, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# deletar algum evento cadstrado atraves do seu ID 
@api_view(['DELETE'])
def delete_eventos(request, pk):
    try:
        eventos = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
       return Response({'Erro': 'Evento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    eventos.delete()
    return Response({'Mensagem': f'O seu {eventos.nome} foi apagado'}, status=status.HTTP_200_OK)