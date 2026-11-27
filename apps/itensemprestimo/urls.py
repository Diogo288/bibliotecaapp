from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'itensemprestimo'

router = routers.SimpleRouter()
router.register('', views.ItemEmprestimoViewSet, basename='itensemprestimo')

urlpatterns = [
    path('', include(router.urls)),
]