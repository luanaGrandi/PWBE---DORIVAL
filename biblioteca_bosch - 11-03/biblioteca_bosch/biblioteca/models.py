from django.db import models

class Cadastro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)
    outros = models.TextField()

    def __str__(self):
        return self.titulo
    
# essa pagina serve para fazer os modelos como os campos de escrita, quantos caracteres poderão ser escrito...