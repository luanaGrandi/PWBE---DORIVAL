from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .serializers import UsuarioSerializer



# ATIVIDADE FEITA COM O PROFESSOR
# @api_view(['POST'])
# def criar_usuario(request):
#     username = request.data.get('username')
#     senha = request.data.get('senha')
#     edv = request.data.get('EDV')
#     data_nascimento = request.data.get('data_nascimento')
#     padrinho = request.data.get('padrinho')
#     apelido = request.data.get('apelido')

#     # verificar os campos que são obrigatorios
#     if not username or not senha or not edv or not data_nascimento:
#         return Response({'Erro': 'Campos obrigatorios imcompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
#     # verificar se o usuario ja existe
#     if UsuarioDS16.objects.filter(username=username).exists():
#         return Response({'Erro': f'username {username} já existe'},  status=status.HTTP_400_BAD_REQUEST)
    
#     # verificar se existe o mesmo edv cadastrado
#     if UsuarioDS16.objects.filter(edv=edv).exists():
#         return Response({'Erro': f'EDV {edv} já existe'},  status=status.HTTP_400_BAD_REQUEST)

#     # criar usuario
#     usuario = UsuarioDS16.objects.create_user(
#         username=username,
#         password=senha,
#         edv = edv,
#         data_nascimento = data_nascimento,
#         padrinho = padrinho,
#         apelido = apelido,
#         email = f"{username}@bosch.com",
#     )
#     return Response({'mensagem': f'Usuario {username} criado com sucesso'},  status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def logar_usuario(request):
#     username = request.data.get('username')
#     senha = request.data.get('senha')

#     usuario = authenticate(username=username, password = senha)

#     if usuario:
#        refresh =  RefreshToken.for_user(usuario)
#        return Response({
#            'acesso': str(refresh.access_token),
#            'refresh' : str(refresh)
#         }, status=status.HTTP_200_OK)
    
#     else:
#         return Response({'erro': 'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def read(request):
#     return Response({"Mensagem": "ola DS16!!"}, status=status.HTTP_200_OK)


# MINHA ATIVIDADE

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    animais = request.data.get('animais')
    escolha_categoria = request.data.get('escolha_categoria')

    # verificar os campos que são obrigatorios
    if not username or not senha or not idade or not escolha_categoria or not telefone:
        return Response({'Erro': 'Campos obrigatorios imcompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    # verificar se o usuario ja existe
    if UsuarioDS16.objects.filter(username=username).exists():
         return Response({'Erro': f'username {username} já existe'},  status=status.HTTP_400_BAD_REQUEST)
    
     # verificar se existe o mesmo edv cadastrado
    if UsuarioDS16.objects.filter(telefone=telefone).exists():
        return Response({'Erro': f'O numero de telefone: {telefone} já existe'},  status=status.HTTP_400_BAD_REQUEST)

   # criar usuario
    usuario = UsuarioDS16.objects.create_user(
        username=username,
        password=senha,
        biografia = biografia,
        idade = idade,
        telefone = telefone,
        endereco = endereco,
        animais = animais,
        categoria = escolha_categoria,
    )
    return Response({'mensagem': f'Usuario {username} criado com sucesso'},  status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password = senha)

    if usuario:
       refresh =  RefreshToken.for_user(usuario)
       return Response({
           'acesso': str(refresh.access_token),
            'refresh' : str(refresh)
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({'erro': 'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuario(request):
    usuarios = UsuarioDS16.objects.all()
    serializer = UsuarioSerializer(usuarios, many = True)
    return Response(serializer.data)


@api_view(['POST']) #criar
@permission_classes([IsAuthenticated])
def create_usuario(resuest):
    if resuest.method == 'POST':
        serializer = UsuarioSerializer(data = resuest.data, many=isinstance(resuest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_usuario(request, pk):
    try:
        usuarios = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
       return Response({'Erro': 'Usuario não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializer(usuarios, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_usuario(request, pk):
    try:
        usuarios = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
       return Response({'Erro': 'usuario não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    usuarios.delete()
    return Response({'Mensagem':'O  usuario foi apagado'}, status=status.HTTP_200_OK)