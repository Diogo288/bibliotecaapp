from rest_framework import viewsets
from .models import Leitor, LeitorRedeSocial
from .serializer import LeitorSerializer, LeitorRedeSocialSerializer

class LeitorViewSet(viewsets.ModelViewSet):
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer

class LeitorRedeSocialViewSet(viewsets.ModelViewSet):
    queryset = LeitorRedeSocial.objects.all()
    serializer_class = LeitorRedeSocialSerializer