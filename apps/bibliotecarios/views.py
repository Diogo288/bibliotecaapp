from rest_framework import viewsets
from .models import Bibliotecario
from .serializer import BibliotecarioSerializer

# Faz o CRUD de bibliotecarios: listar, criar, ver, editar e apagar

class BibliotecarioViewSet(viewsets.ModelViewSet):
    queryset = Bibliotecario.objects.all()
    serializer_class = BibliotecarioSerializer