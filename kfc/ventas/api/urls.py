from rest_framework.routers import DefaultRouter
from ventas.api.views import VentasViewSet

router = DefaultRouter()
router.register(r'ventas', VentasViewSet, basename='ventas')
urlpatterns = router.urls