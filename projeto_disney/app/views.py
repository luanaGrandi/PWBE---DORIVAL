from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, IngressoSerializer,LoginSerializer
from .permissions import IsGestor,IsGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Ingresso
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    # pegar todos os usuarios
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]


class IngressoRUDAPIView(RetrieveUpdateDestroyAPIView):
    # pega todos os ingressos
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]

class IngressoListCreateAPIView(ListCreateAPIView):
    # pegar todos os ingressos
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        # so pode criar ingressso se for gestor
        if self.request.method == 'GET':
            return [IsAuthenticated()] #AllowAny -> qualquer um pode fazer a consulta
        return [IsGestor()]






# ----------------------------------------------------------------------------------------
# serializer_class = UsuarioSerializer
# # permission_classes = [IsGestor]
# def get_permissions(self):
#     if self.request.method == 'GET':
#         return [IsAuthenticated()]
#     return [IsGestor]
# # o usuario que for autenticado pode fazer o get, mas se não for, só o gestor pode fazer