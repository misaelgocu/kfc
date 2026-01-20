from rest_framework import viewsets
from ventas.models import Empresas, Marcas, Sucursales, Ventas
from ventas.api.serializers import (
    EmpresasSerializer,
    MarcasSerializer,
    SucursalesSerializer,
    VentasSerializer
    )

# from kfc.models import Ventas
# from kfc.api.serializers import VentasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer

class SucursalesViewSet(viewsets.ModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer
