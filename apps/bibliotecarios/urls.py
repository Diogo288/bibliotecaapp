from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'bibliotecarios'

router = routers.SimpleRouter()
router.register('', views.BibliotecarioViewSet, basename='bibliotecarios')

urlpatterns = [
    path('', include(router.urls)),
]