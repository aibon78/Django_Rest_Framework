from rest_framework import serializers
from escola.models import Estudante,Curso  


class EstudanteSerielizers(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        field = ['id','nome','email','cpf','data_nascimento','celular']
        
class CursoSerielizers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'