from django.db import models
from core.models import BaseModelWithSoftDelete


class Curso(BaseModelWithSoftDelete):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(BaseModelWithSoftDelete):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,null=True)

    def apresentar(self):
        return f'olá,meu nome é {self.nome} e tenho {self.idade} anos'
    
    def __str__(self):
        return self.nome