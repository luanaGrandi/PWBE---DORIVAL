from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Sala, ReservaAmbiente, Disciplina
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer,LoginSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # só o gestor tera permissao de criar e listar
    permission_classes = [IsGestor]

# essa class vai consultar o usuario pelo Id, e fazer o GET, PUT e o DELETE
class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    # procurar pela pk (id do usuario)
    lookup_field = 'pk'

# class para listar todas as disciplinas ou cria-las
class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

# essa class vai  fazer o GET, PUT, DELETE e o PACTH
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

# listagem das disciplinas que o professor tem 
class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        # filtrar todas as disciplinas do usuario(professor)
        return Disciplina.objects.filter(professor = self.request.user)

# ver todos os ambientes reservdos ou cria-los
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return[IsGestor()]
    
    # ver reserva do professor: exemplo professor , id 5 (ira listar os ambientes reservados do professor do id 5)
    def get_queryset(self):
    # def get_queryset(self): -> definir a consulta que ele vai fazer
        queryset =  super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            # filtrar ambiente especifico de um professor
            queryset = queryset.filter(professor_id=professor_id)
        return queryset
    
# essa class pode fazer o GET, PUT, DELETE e o PACTH da reserva de ambiente
class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field = 'pk'

# listagem da reserva de ambientes que o professor tem
class ReservaAmbienteProfessorList(ListAPIView):

    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        # filtrar as reservas de um professor especifico
        return ReservaAmbiente.objects.filter(professor = self.request.user)
    

class loginView(TokenObtainPairView):
    serializer_class = LoginSerializer

