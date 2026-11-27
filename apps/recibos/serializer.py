from rest_framework import serializers
from .models import Recibo

# Converte objetos Recibo em JSON e valida o JSON recebido

class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibo
        fields = '__all__'