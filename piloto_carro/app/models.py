from django.db import models
# importação das models


# class piloto
class Piloto (models.Model):
    # atributos do piloto 
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    classificacao = models.PositiveIntegerField()
    equipe= models.CharField(max_length=255)
    
    # retornar o nome e a posição que o piloto ficou
    def __str__(self):
        return f'{self.nome} esta na {self.classificacao} posição'


# classs carro
class Carro(models.Model):
    # atributos do carro
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)

    # filtro de escolha das cores do carro
    escolha_cores = (
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'rosa'),
        ('BRANCO', 'branco'),
        ('PRETO', 'preto'),
        ('VERDE', 'verde'),
        ('ROXO', 'roxo'),
        ('CINZA', 'cinza')
    )
    cor = models.CharField(max_length=50, choices=escolha_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)


