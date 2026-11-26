from rest_framework import serializers
from .models import Livro

# Converte objetos Livro em JSON e valida o JSON recebido

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'