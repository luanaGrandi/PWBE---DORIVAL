from django.db import models

class Tarefas(models.Model):
    status =  models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status