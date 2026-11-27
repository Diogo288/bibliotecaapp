from rest_framework import serializers
from .models import ItemEmprestimo

# Converte objetos ItemEmprestimo em JSON; o subtotal aparece so para leitura

class ItemEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEmprestimo
        fields = '__all__'