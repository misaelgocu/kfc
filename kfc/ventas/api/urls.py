from rest_framework.routers import DefaultRouter
from ventas.api.views import (
    EmpresasViewSet,
    MarcasViewSet,
    SucursalesViewSet,
    VentasViewSet
    )

router = DefaultRouter()
router.register(r'empresas', EmpresasViewSet, basename='empresas')
router.register(r'marcas', MarcasViewSet, basename='marcas')
router.register(r'sucursales', SucursalesViewSet, basename='sucursales')
router.register(r'ventas', VentasViewSet, basename='ventas')
urlpatterns = router.urls