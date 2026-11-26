from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'redessociais'

router = routers.SimpleRouter()
router.register('', views.RedeSocialViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls)),
]