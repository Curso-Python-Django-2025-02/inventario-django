from rest_framework import serializers

from activos.models import Activo, Ubicacion

class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activo
        fields = ['id', 'nombre', 'num_serie', 'estado', 'fecha_adquisicion', 'valor', 'ubicacion']

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['id', 'lugar']
