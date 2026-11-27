from rest_framework import viewsets
from .models import Recibo
from .serializer import ReciboSerializer

# Faz o CRUD de recibos: listar, criar, ver, editar e apagar

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer