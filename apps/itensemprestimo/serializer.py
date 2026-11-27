from rest_framework import serializers
from .models import ItemEmprestimo

class ItemEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEmprestimo
        fields = '__all__'