from rest_framework import viewsets
from .models import Emprestimo
from .serializer import EmprestimoSerializer

# Faz o CRUD de emprestimos: listar, criar, ver, editar e apagar

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer