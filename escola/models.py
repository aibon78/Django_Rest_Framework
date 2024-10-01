from django.db import models

'''Dados necessários:

Id
Nome
E-mail
Não pode estar em branco
CPF
Máximo de 11 caracteres
Data de Nascimento
Número de Celular
Máximo de 14 caracteres'''

class Estudante(models.Model):
    nome = models.CharField(max_length= 100)
    email = models.EmailField(blank = False, max_length=100)
    cpf = models.CharField(max_length= 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length= 14)
    
    def __str__(self):
        return self.nome

'''Dados necessários:
Id
Código
Máximo de 10 caracteres
Descrição
Não pode estar em Branco
Nível (Básico, Intermediário e Avançado)
Não pode estar em Branco
Não pode ser Nulo
Por padrão deve ser Básico'''    

class Curso(models.Model):
    NIVEL= (
        ('B','Básico'),
        ('I', 'Intermediario'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length= 10)
    descricao =models.CharField(max_length= 100, blank = False)
    nivel = models.CharField(max_length= 1, choices=NIVEL, blank=False, null= False, default= 'B')
    
    def __str__(self):
        return self.codigo
    