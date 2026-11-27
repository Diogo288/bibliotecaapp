from rest_framework import viewsets
from .models import ItemEmprestimo
from .serializer import ItemEmprestimoSerializer

class ItemEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = ItemEmprestimo.objects.all()
    serializer_class = ItemEmprestimoSerializer