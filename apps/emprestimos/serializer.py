from rest_framework import serializers
from .models import Emprestimo

# Converte objetos Emprestimo em JSON e valida o JSON recebido

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'