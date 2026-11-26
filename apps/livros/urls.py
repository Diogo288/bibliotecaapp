from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'livros'

router = routers.SimpleRouter()
router.register('', views.LivroViewSet, basename='livros')

urlpatterns = [
    path('', include(router.urls)),
]