from rest_framework import serializers
from .models import Bibliotecario

# Converte objetos Bibliotecario em JSON e valida o JSON recebido

class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = '__all__'