from rest_framework import serializers
from .models import RedeSocial

class RedeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeSocial
        fields = '__all__'