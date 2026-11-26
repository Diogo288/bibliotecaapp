from rest_framework import serializers
from .models import Leitor, LeitorRedeSocial

# Converte objetos Leitor em JSON e valida o JSON recebido

class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = '__all__'

# Converte o vinculo entre leitor e rede social em JSON

class LeitorRedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeitorRedeSocial
        fields = '__all__'