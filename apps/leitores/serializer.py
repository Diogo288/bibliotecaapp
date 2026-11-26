from rest_framework import serializers
from .models import Leitor, LeitorRedeSocial

class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = '__all__'

class LeitorRedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeitorRedeSocial
        fields = '__all__'