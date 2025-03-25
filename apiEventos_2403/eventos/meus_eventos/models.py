from django.db import models

# criando o modelo e seus atributod
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataHora = models.DateTimeField()
    local = models.TextField()
    # para fazer a categoria de escolha
    escolha_categoria = (
        ('Musica', 'Musica'),
        ('Palestra', 'Palestra'),
        ('Workshop', 'Workshop'),
        )
    categoria = models.CharField(max_length=9, choices=escolha_categoria)
    
    # retorna o nome do seu evento que cadastrou
    def __str__(self):
        return self.nome
    


