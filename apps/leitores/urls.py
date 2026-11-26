from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'leitores'

router = routers.SimpleRouter()
router.register('redessociais', views.LeitorRedeSocialViewSet, basename='leitores-redessociais')
router.register('', views.LeitorViewSet, basename='leitores')

urlpatterns = [
    path('', include(router.urls)),
]