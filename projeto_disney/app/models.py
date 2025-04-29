from django.db import models
from django.contrib.auth.models import AbstractUser


class Empresa (models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)




# AbstractUser -> criar um usuario personalizado
class Usuario(AbstractUser):
    # atributos do usuario
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    # filtro de genero
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'),('F', 'Feminino'),('N', 'Prefiro não informar')), null=True, blank=True)

    # filtro de funcao do colaborador
    escolha_colaborador = (
        ('G', 'Gestor'),
        ('E', 'Estagiario'),
        ('A', 'Aprendiz'),
        ('M', 'Meio oficial'),
        
    )
    colaborador = models.CharField(max_length=1, choices=escolha_colaborador, default='A')
    # default -> se caso não passado o valor ele colocara esse valor 'A'

    # campos obrigatorios
    REQUIRED_FIELDS = ['colaborador']

    # chave primaria da class Empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)


class Ingresso(models.Model):
    nome = models.CharField(max_length=100)
    # chave estrangeira
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

