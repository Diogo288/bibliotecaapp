from rest_framework import viewsets
from .models import Leitor, LeitorRedeSocial
from .serializer import LeitorSerializer, LeitorRedeSocialSerializer

# Faz o CRUD de leitores: listar, criar, ver, editar e apagar

class LeitorViewSet(viewsets.ModelViewSet):
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
    
# Faz o CRUD dos vinculos entre leitor e rede social
    
class LeitorRedeSocialViewSet(viewsets.ModelViewSet):
    queryset = LeitorRedeSocial.objects.all()
    serializer_class = LeitorRedeSocialSerializer