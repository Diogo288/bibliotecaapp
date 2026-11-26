from rest_framework import serializers
from .models import RedeSocial

# Converte objetos RedeSocial em JSON e valida o JSON recebido

class RedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = '__all__'