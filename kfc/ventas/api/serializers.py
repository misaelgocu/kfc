from rest_framework import serializers
from ventas.models import  Empresas, Marcas, Sucursales, Ventas


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'

class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'