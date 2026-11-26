from rest_framework import viewsets
from .models import RedeSocial
from .serializer import RedeSocialSerializer

# Faz o CRUD de redes sociais: listar, criar, ver, editar e apagar

class RedeSocialViewSet(viewsets.ModelViewSet):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer