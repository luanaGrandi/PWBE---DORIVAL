from django.db import models
from django.contrib.auth.models import AbstractUser


# Abstractuser = usuario abstrato
class UsuarioDS16(AbstractUser):
    # ATIVIDADE COM O PROFESSOR
    # data_nascimento = models.DateField()
    # edv = models.PositiveBigIntegerField()
    # padrinho = models.CharField(max_length=255, null=True, blank=True)
    # apelido = models.CharField(max_length=255, null=True, blank=True)


    # MINHA ATIVIDADE
    nome = models.CharField(max_length=255)
    biografia = models.TextField(null=True, blank=True)
    idade = models.PositiveIntegerField( null=True, blank=True)
    telefone = models.PositiveBigIntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=255)
    animais = models.PositiveIntegerField(null=True, blank=True)
    escolha_categoria = (
        ('Ensino fundamental', 'Ensino fundamental'),
        ('ensino Médio', 'ensino Médio'),
        ('Ensino superior', 'Ensino superior'),
        ('Ensino tecnico', 'Ensino tecnico'),
        )
    categoria = models.CharField(max_length=23, choices=escolha_categoria)

    # todo campo que é obrigatorio, precisa colocar dentro do REQUIRED_FIELDS
    REQUIRED_FIELDS = ['nome', 'idade','telefone']

    def __str__(self):
        return self.nome
