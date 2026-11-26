from rest_framework import viewsets
from .models import Livro
from .serializer import LivroSerializer

# Faz o CRUD de livros: listar, criar, ver, editar e apagar

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer