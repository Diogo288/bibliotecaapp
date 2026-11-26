from rest_framework import viewsets
from .models import RedeSocial
from .serializer import RedeSocialSerializer

class RedeSocialViewSet(viewsets.ModelViewSet):
    queryset = RedeSocial.objects.all()
    serializer_class = RedeSocialSerializer