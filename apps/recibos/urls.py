from rest_framework.routers import SimpleRouter
from . import views

app_name = 'recibos'

router = SimpleRouter()
router.register('', views.ReciboViewSet, basename='recibos')

urlpatterns = router.urls