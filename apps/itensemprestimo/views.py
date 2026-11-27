from rest_framework import viewsets
from .models import ItemEmprestimo
from .serializer import ItemEmprestimoSerializer

# Faz o CRUD dos itens de emprestimo: listar, criar, ver, editar e apagar

class ItemEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = ItemEmprestimo.objects.all()
    serializer_class = ItemEmprestimoSerializer