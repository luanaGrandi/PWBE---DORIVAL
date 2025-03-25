from django.db import models


#  criar o modelo 
class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qntRodas = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=255)
    # lista de escolha para combustivel
    escolha_combustivel = (
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('GNV', 'GNV'),
        ('ELETRICO', 'Eletrico'),
        ('ALCOOL', 'alcool'),
        ('DIESEL', 'diesel'),
        ('FB', 'Feedback'),
        )
    combustivel = models.CharField(max_length=9, choices=escolha_combustivel)
    
    def __str__(self):
        return self.nome
    

