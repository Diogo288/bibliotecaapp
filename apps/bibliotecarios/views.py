from rest_framework import viewsets
from .models import Bibliotecario
from .serializer import BibliotecarioSerializer

class BibliotecarioViewSet(viewsets.ModelViewSet):
    queryset = Bibliotecario.objects.all()
    serializer_class = BibliotecarioSerializer