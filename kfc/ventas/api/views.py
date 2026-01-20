from rest_framework import viewsets
from ventas.models import Ventas
from ventas.api.serializers import VentasSerializer

# from kfc.models import Ventas
# from kfc.api.serializers import VentasSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer
