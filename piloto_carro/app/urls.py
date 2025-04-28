from django.contrib import admin
from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView, CarroListCreateAPIView,CarroRetrieveUpdateDestroyAPIView
# importação das views

# paremetros das rotas
urlpatterns = [
    # Rota para a pagina de criar o piloto
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    # rota para filtrar o piloto atraves do seu pk
    path('piloto/<int:pk>/', view=PilotoRetrieveUpdateDestroyAPIView.as_view()),
    # Rota para a pagina de criar o carro
    path('carro/', view=CarroListCreateAPIView.as_view()),
    # rota para filtrar o carro atraves do seu pk
    path('carro/<int:pk>/', view=CarroRetrieveUpdateDestroyAPIView.as_view()),
]