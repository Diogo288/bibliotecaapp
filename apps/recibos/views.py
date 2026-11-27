from rest_framework import viewsets
from .models import Recibo
from .serializer import ReciboSerializer

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer