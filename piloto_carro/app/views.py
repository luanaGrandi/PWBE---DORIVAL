from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



#  CLASS DO PILOTO

# essa class define a paginação do piloto
class PilotoPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


#  essa class faz a atualização e o delete de eum unico piloto atraves do seu Id/pk
class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    # GET
    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'not found',
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



#  essa class lista e cria os pilotos
class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    @swagger_auto_schema(
            operation_description='lista todos os pilotos da formula 1',
            responses={
                200: PilotoSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_PATH,
                    description='filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )

            ]  
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Cria um novo piloto',
            request_body=PilotoSerializer,
            responses={
                201: PilotoSerializer,
                400: 'ERROR'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('somente a DS16 deve ficar entre os 5')
        serializer.save()


#  CLASS DO CARRO

# essa class define a paginação do piloto
class CarroPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

#  essa class faz a atualização e o delete de eum unico piloto atraves do seu Id/pk
class CarroRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'pk'

    # GET
    @swagger_auto_schema(
        operation_description='Pega o carro do ID fornecido',
        responses={
            200: CarroSerializer,
            404: 'not found',
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



#  essa class lista e cria os pilotos
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    @swagger_auto_schema(
            operation_description='lista todos os pilotos da formula 1',
            responses={
                200: CarroSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_PATH,
                    description='filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )

            ]  
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Cria um novo piloto',
            request_body=CarroSerializer,
            responses={
                201: CarroSerializer,
                400: 'ERROR'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset


      